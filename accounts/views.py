from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import Account
from accounts.forms import RegisterForm


def home_view(request):
    return HttpResponse('Hello')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)
