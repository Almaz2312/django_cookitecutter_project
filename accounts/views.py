from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse


from .forms import CustomUserCreationForm


def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'GET':
        return render(
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)
            return redirect(reverse('dashboard'))


def see_request(request):
    text = f"""
        Some attributes of HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")


def see_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:       {request.user.username}
        is_anonymous:   {request.user.is_anonymous}
        is_staff:       {request.user.is_staff}
        is_superuser:   {request.user.is_superuser}
        is_active:      {request.user.is_active}
    """

    return HttpResponse(text, content_type='text/plain')


@login_required
def private_place(request):
    return HttpResponse("Shhhh, members only!!!", content_type='text/plain')


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employee must wash hands", content_type='text/plain')


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f'Hello {username}')
    messages.add_message(request, messages.WARNING, 'DANGER WILL ROBINSON')

    return HttpResponse('Messages added', content_type='text/plain')
