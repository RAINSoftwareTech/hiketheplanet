from rest_framework.exceptions import APIException
from rest_framework import status

from django.utils.translation import gettext_lazy as _
class BadRequest(APIException):
    """Basic Bad Request exception"""
    status_code = status.HTTP_400_BAD_REQUEST
    error = _('Bad Request')
    default_detail = _(
        'The browser (or proxy) sent a request that this server could '
        'not understand.'
    )
    default_code = 'bad_request'

    def __init__(self, detail=None, code=None):
        super(BadRequest, self).__init__(detail, code)
        self.detail = {'error': self.error, 'description': self.detail}