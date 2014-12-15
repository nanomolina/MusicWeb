from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import redirect


def home(request):
    return render_to_response('core/home.html',
                              RequestContext(request))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            response = redirect('core:login')
        else:
            response = render_to_response(
                'registration/signup.html',
                RequestContext(request, {'creation_form': form})
            )
        return response
    context = {'creation_form': form}
    return render_to_response(
        'registration/signup.html',
        RequestContext(request, context)
    )
