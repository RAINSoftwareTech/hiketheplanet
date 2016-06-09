# -*- coding: utf-8 -*-

from uuid import uuid4

from django.conf import settings
from django.core.exceptions import ValidationError, ImproperlyConfigured


def setup_view(view, request, *args, **kwargs):
    """Mimic as_view() returned callable, but returns view instance.

    args and kwargs are the same you would pass to ``reverse()``
    Borrowed from: http://tech.novapost.fr/django-unit-test-your-views-en.html
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


def get_max_mb(mb_size_limit):
    try:
        max_mb = settings.MAX_UPLOAD_SIZE_IN_MB
        if mb_size_limit and mb_size_limit < max_mb:
            max_mb = mb_size_limit
        return max_mb
    except AttributeError:
        if not mb_size_limit:
            raise ImproperlyConfigured('You must define a max file size in '
                                       'either settings or the model field '
                                       'validator.')
        else:
            return mb_size_limit


def get_file_attr(obj):
    try:
        return obj.file
    except AttributeError:
        raise ImproperlyConfigured('This validator is only for use on file '
                                   'or image fields.')


def validate_file_upload_size(upload_obj, mb_size_limit=None):
    file_size = get_file_attr(upload_obj).size
    max_mb = get_max_mb(mb_size_limit)
    if file_size > max_mb * 1024 * 1024:
        raise ValidationError('File too large. '
                              'Max file upload size '
                              'is {}MB'.format(str(max_mb)))


def validate_file_has_extension(upload_obj):
    if '.' not in get_file_attr(upload_obj).name:
        raise ValidationError('You are attempting to upload a file that has '
                              'no extension.')


def randomize_filename(filename):
    ext = filename.split('.')[-1]
    return '{0}.{1}'.format(uuid4().hex, ext)


def user_directory_path(instance):
    # file will be uploaded to
    # MEDIA_ROOT/hikers/hiker_slug/model_name/<filename>
    try:
        return '{0}/{1}'.format('hikers',
                                instance.hiker.slug)
    except AttributeError:
        raise ImproperlyConfigured('You are attempting to use an upload_to '
                                   'method that expects a Hiker with an '
                                   'object that does not have a '
                                   'hiker attribute')


def profile_pics_upload_path(instance, filename):
    hiker_path = user_directory_path(instance)
    return '{0}/profile_pics/{1}'.format(hiker_path,
                                         randomize_filename(filename))


def hiker_photos_upload_path(instance, filename):
    hiker_path = user_directory_path(instance)
    return '{0}/hike_photos/{1}'.format(hiker_path,
                                        randomize_filename(filename))


def hike_directory_path(instance):
    # file path for hike media
    # MEDIA_ROOT/region_slug/trailhead_slug/hike_slug/
    try:
        return '{0}/{1}/{2}/{3}'.format('hikes',
                                        instance.hike.trailhead.region.slug,
                                        instance.hike.trailhead.slug,
                                        instance.hike.slug)
    except AttributeError:
        raise ImproperlyConfigured('You are attempting to use an upload_to '
                                   'method that expects a Hike with an '
                                   'object that does not have a '
                                   'hike attribute')


def trail_map_upload_path(instance, filename):
    hike_path = hike_directory_path(instance)
    return '{0}/trail_maps/{1}'.format(hike_path,
                                       randomize_filename(filename))


def hike_photo_upload_path(instance, filename):
    hike_path = hike_directory_path(instance)
    return '{0}/photos/{1}'.format(hike_path,
                                   randomize_filename(filename))
