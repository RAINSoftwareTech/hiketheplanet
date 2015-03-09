from django.shortcuts import render_to_response


def loggedin(request):
    return render_to_response('hikes/index.html', {'username': request.user.username})


