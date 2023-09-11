from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def loginView(request):
    context = {}
    return render(request, 'Login/index.html', context)

def do_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('indexView')
        else:
            messages.add_message(request, messages.WARNING, 'Usuário ou senha errado!')
            context = {}
            return render(request, 'Login/index.html', context)

@login_required
def logout_view(request):
    logout(request)
    context = {}
    return redirect('login_view')
