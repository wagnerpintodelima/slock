from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def newView(request):
    context = {}
    return render(request, 'Company/new.html', context)
