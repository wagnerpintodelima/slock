from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def indexView(request):
    context = {}
    return render(request, 'Dashboard/index.html', context)
