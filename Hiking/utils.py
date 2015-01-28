# simple functions that may be needed by all apps


def encode_url(name):
    to_keep = 'abcdefghijklmnopqrstuvwxyz '
    lower_name = name.lower()
    clean_name = lower_name
    for char in lower_name:
        if char not in to_keep:
            clean_name = lower_name.replace(char, '')
    clean_name = clean_name.replace('  ', ' ')
    return clean_name.replace(' ', '_')


def decode_url(url, field_list):
    url_name = url.replace('_', ' ')
    url_name = url_name.title()
    for name in field_list:
        for i in range(len(name) - 1, -1, -1):
            if name.startswith(url_name[:i]):
                if url == encode_url(name):
                    return name
    return url_name


def build_context_dict(this_model, url, key):
    names_list = this_model.objects.values_list('name', flat=True)
    this_name = decode_url(url, names_list)
    return {key: this_name}
