# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.test import TestCase
from django.test.utils import override_settings
from mock import MagicMock, patch

from core.tests.test_models import TestSlugifiedName
from core.utils import (validate_file_upload_size, get_max_mb,
                        randomize_filename, user_directory_path,
                        profile_pics_upload_path, hiker_photos_upload_path,
                        hike_directory_path, hike_photo_upload_path,
                        trail_map_upload_path, get_file_attr,
                        validate_file_has_extension)

from hikers.tests.factories import HikerFactory


class CoreUtilsTests(TestCase):

    def test_get_file_attr(self):
        mock_upload_obj = 'CharField'
        with self.assertRaises(ImproperlyConfigured):
            get_file_attr(mock_upload_obj)

        mock_upload_obj = MagicMock()
        mock_upload_obj.file = MagicMock()
        self.assertEquals(get_file_attr(mock_upload_obj), mock_upload_obj.file)

    @patch('core.utils.get_file_attr')
    @patch('core.utils.get_max_mb')
    def test_validate_file_upload_size(self, mock_max_mb, mock_file_attr):
        mock_upload_obj = MagicMock()
        mock_file = MagicMock()
        mock_file.size = 6 * 1024 * 1024
        mock_file_attr.return_value = mock_file
        mock_max_mb.return_value = 5
        with self.assertRaises(ValidationError):
            validate_file_upload_size(mock_upload_obj)

    @override_settings(MAX_UPLOAD_SIZE_IN_MB=4)
    def test_get_max_mb_with_settings(self):
        mb_size = None
        self.assertEquals(get_max_mb(mb_size), 4)
        mb_size = 3
        self.assertEquals(get_max_mb(mb_size), 3)
        mb_size = 5
        self.assertEquals(get_max_mb(mb_size), 4)

    def test_get_max_nb_without_settings(self):
        mb_size = None
        with self.assertRaises(ImproperlyConfigured):
            get_max_mb(mb_size)
        mb_size = 7
        self.assertEquals(get_max_mb(mb_size), mb_size)

    def test_randomize_filename(self):
        name = 'myrandomfile'
        ext = 'jpg'
        filename = '{}.{}'.format(name, ext)
        self.assertNotIn(name, randomize_filename(filename))
        self.assertIn(ext, randomize_filename(filename))

    @patch('core.utils.get_file_attr')
    def test_validate_file_ext(self, mock_file_attr):
        name = 'myrandomfile'
        mock_upload_obj = MagicMock()
        mock_file = MagicMock()
        mock_file.name = name
        mock_file_attr.return_value = mock_file
        with self.assertRaises(ValidationError):
            validate_file_has_extension(mock_upload_obj)

    def test_user_directory_path(self):
        instance = TestSlugifiedName()
        with self.assertRaises(ImproperlyConfigured):
            user_directory_path(instance)

        instance = HikerFactory()
        self.assertIn(instance.slug, user_directory_path(instance))

        instance = MagicMock()
        instance.hiker = MagicMock()
        instance.hiker.slug = 'hiker-slug'
        self.assertIn(instance.hiker.slug, user_directory_path(instance))

    @patch('core.utils.user_directory_path')
    @patch('core.utils.randomize_filename')
    def test_profile_pics_upload_path(self, mock_file_name, mock_path):
        mock_file_name.return_value = 'file-name'
        mock_path.return_value = 'user/path'
        self.assertIn('profile_pics',
                      profile_pics_upload_path('instance', 'filename'))

    @patch('core.utils.user_directory_path')
    @patch('core.utils.randomize_filename')
    def test_hiker_photos_upload_path(self, mock_file_name, mock_path):
        mock_file_name.return_value = 'file-name'
        mock_path.return_value = 'user/path'
        self.assertIn('hike_photos',
                      hiker_photos_upload_path('instance', 'filename'))

    def test_hike_directory_path(self):
        instance = TestSlugifiedName()
        with self.assertRaises(ImproperlyConfigured):
            hike_directory_path(instance)
        instance = MagicMock()
        instance.hike = MagicMock()
        instance.hike.slug = 'hike-slug'
        instance.hike.trailhead = MagicMock()
        instance.hike.trailhead.slug = 'trailhead-slug'
        instance.hike.trailhead.region = MagicMock()
        instance.hike.trailhead.region.slug = 'region-slug'
        self.assertIn('hikes', hike_directory_path(instance))

    @patch('core.utils.hike_directory_path')
    @patch('core.utils.randomize_filename')
    def test_trail_map_upload_path(self, mock_file_name, mock_path):
        mock_file_name.return_value = 'file-name'
        mock_path.return_value = 'hike/path'
        self.assertIn('trail_maps',
                      trail_map_upload_path('instance', 'filename'))

    @patch('core.utils.hike_directory_path')
    @patch('core.utils.randomize_filename')
    def test_hike_photo_upload_path(self, mock_file_name, mock_path):
        mock_file_name.return_value = 'file-name'
        mock_path.return_value = 'hike/path'
        self.assertIn('photos',
                      hike_photo_upload_path('instance', 'filename'))
