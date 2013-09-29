# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def index(request):
    """
    Demo page index view.
    Process sign in and sign up forms.
    """
    auth_form = reg_form = None
    if request.method == 'POST':
        action = request.POST.get('action', '')
        print action
        if action == 'sign-in':
            auth_form = AuthenticationForm(data=request.POST)
            if auth_form.is_valid():
                login(request, auth_form.get_user())
        elif action == 'sign-up':
            reg_form = UserCreationForm(data=request.POST)
            if reg_form.is_valid():
                user = reg_form.save()
                user = authenticate(username=reg_form.cleaned_data['username'], 
                             password=reg_form.cleaned_data['password1'])
                login(request, user)

    context = {}
    context['auth_form'] = auth_form or AuthenticationForm()
    context['reg_form'] = reg_form or UserCreationForm()
    return render_to_response('index/index.html', context, 
                                context_instance=RequestContext(request))