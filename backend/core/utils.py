# -*- coding: utf-8 -*-

# Imports from Django
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.text import slugify

# Imports from Third Party Modules
import re
from datetime import datetime
from uuid import uuid4


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
            msg = (
                'You must define a max file size in either settings or the '
                'model field validator.'
            )
            raise ImproperlyConfigured(msg)
        else:
            return mb_size_limit


def get_file_attr(obj):
    try:
        return obj.file
    except AttributeError:
        msg = 'This validator is only for use on file or image fields.'
        raise ImproperlyConfigured(msg)


def validate_file_upload_size(upload_obj, mb_size_limit=None):
    file_size = get_file_attr(upload_obj).size
    max_mb = get_max_mb(mb_size_limit)
    if file_size > max_mb * 1024 * 1024:
        msg = f'File too large. Max file upload size is {max_mb}MB'
        raise ValidationError(msg)


def validate_file_has_extension(upload_obj):
    if '.' not in get_file_attr(upload_obj).name:
        msg = 'You are attempting to upload a file that has no extension.'
        raise ValidationError(msg)


def randomize_filename(filename):
    ext = filename.split('.')[-1]
    return f'{uuid4().hex}.{ext}'


def user_directory_path(instance):
    # file will be uploaded to
    # MEDIA_ROOT/hikers/hiker_slug/model_name/<filename>
    Hiker = apps.get_model('hikers', 'Hiker')
    if isinstance(instance, Hiker):
        return f'hikers/{instance.slug}'

    try:
        return f'hikers/{instance.hiker.slug}'
    except AttributeError:
        msg = (
            'You are attempting to use an upload_to method that expects '
            'a Hiker with an object that does not have a hiker attribute'
        )
        raise ImproperlyConfigured(msg)


def profile_pics_upload_path(instance, filename):
    hiker_path = user_directory_path(instance)
    return f'{hiker_path}/profile_pics/{randomize_filename(filename)}'


def hiker_photos_upload_path(instance, filename):
    hiker_path = user_directory_path(instance)
    return f'{hiker_path}/hike_photos/{randomize_filename(filename)}'


def unique_slugify(queryset, slug_text):
    slug = slugify(truncate_slug_text(slug_text))
    count = queryset.filter(slug__startswith=slug).count()
    if count == 0:
        return slug

    unique_slug = f'{slug}-{count}'
    while queryset.filter(slug=unique_slug).exists():
        count += 1
        unique_slug = f'{slug}-{count}'
    return unique_slug


def title_hike_or_date_str(obj):
    """Receives a instance object from any model that contains the following
    attributes: 'hike', 'title', 'created'
    :param obj: model instance with attributes: 'hike', 'title', 'created'
    :return: unicode suitable string
    """
    try:
        if not obj.pk:
            uni_date = datetime.today().date().isoformat()
        else:
            uni_date = obj.created.date().isoformat()

        params = [obj.title, obj.hike.name, uni_date]
        params = [p for p in params if p]
        return ' - '.join(params[:2])
    except AttributeError:
        msg = (
            'You are attempting to use a unicode creation method on a '
            'model that is does not have one of the following attributes: '
            '"title", "hike", or "created".'
        )
        raise ImproperlyConfigured(msg)


def truncate_slug_text(slug_text, parts_char='-'):
    """Assumes that the first, second and last sections of slug_text are the
    important parts to build a slug from.
    :param slug_text: text, such as the return from __str__ to be converted
    to slug
    :param parts_char: optional character that separates sections of slug_text
        default is '-'
    :return: string with max 3 sections from slug_text truncated to 50 chars
    """
    slug_max = 50
    if len(slug_text) <= slug_max:  # already within max range, return whole
        return slug_text

    date_reg_exp = re.compile(r'\d{4}[-/]\d{2}[-/]\d{2}')
    all_dates = date_reg_exp.findall(slug_text)
    new_slug_text = []
    if all_dates:
        new_slug_text.append(all_dates[-1])  # if dates, keep the last date
        slug_max -= len(new_slug_text[0]) + 1  # pad by one for join char
        for date in all_dates:  # then remove all dates from starting text
            re.sub(date, '', slug_text)

    slug_parts = slug_text.split(parts_char)
    if len(slug_parts) == 1 and not all_dates:
        # only one section found, simple truncation
        return slug_text[:slug_max]

    if len(slug_parts) >= 2:
        # middle section: not as important as beginning or date
        new_slug_text.insert(0, slug_parts[1][:15])
        slug_max -= len(new_slug_text[0]) + 1  # pad by one for join char

    # simple truncation of beginning up to remaining max characters
    new_slug_text.insert(0, slug_parts[0][:slug_max])
    return '-'.join(new_slug_text)
