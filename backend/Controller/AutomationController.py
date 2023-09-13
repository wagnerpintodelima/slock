from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from backend.models import Automation


def newView(request):
    context = {}
    return render(request, 'Automation/new.html', context)


@login_required
def SaveAction(request):

    if request.method == 'POST':
        name = request.POST.get('name', None)
        short_name = request.POST.get('short_name', None)
        ip = request.POST.get('ip', None)
        subnet = request.POST.get('subnet', None)
        gateway = request.POST.get('gateway', None)
        mac = request.POST.get('mac', None)
        type_location = request.POST.get('type_location', 0)
        description = request.POST.get('description', None)
        status = request.POST.get('status', 0)

        item = Automation()
        item.name = name
        item.ip = ip
        item.subnet = subnet
        item.gateway = gateway
        item.mac = mac
        item.short_name = short_name
        item.description = description
        item.type_location = type_location
        item.status = status
        item.created_by = request.user.id
        item.save()

        messages.add_message(request, messages.SUCCESS, 'Registro salvo com sucesso!')

    return redirect('AutomationNewAction')
