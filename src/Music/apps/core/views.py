from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required


def home(request):
    return render_to_response('core/home.html',
                              RequestContext(request))

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('core:home')
        else:
            return HttpResponse("Login Error")
