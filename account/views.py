# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpRequest, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, reverse






def custreg(request):
    if request.method == 'POST' :
        form = cust_reg_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            usr = auth.authenticate(username=username, password=password)
            auth.login(request, usr)
            return render(request, 'welcome.html')

    else:
        form = cust_reg_form()
    return render(request, 'reg.html', {'form': form})


def login(request):
    if request.method == "POST" :
        username = request.POST['user']
        password = request.POST['psk']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('welcome'))
            else:
                messages.error(request, 'Username or password didn\'t match.')

        except auth.ObjectDoesNotExist:
            print("invalid user")

    return render(request, 'login.html')

@login_required(login_url="/account/login")
def welcome(request):
    return render(request, 'welcome.html')


@login_required(login_url="/account/login")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')