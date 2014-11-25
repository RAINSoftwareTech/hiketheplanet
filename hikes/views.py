from django.shortcuts import render_to_response
from django.template import RequestContext
from hikes.forms import UserForm, HikerRegistrationForm


def register(request):
    context = RequestContext(request)
    registered = False

    pass


def index(request):
    context = RequestContext(request)
    return render_to_response('hikes/index.html', context)


