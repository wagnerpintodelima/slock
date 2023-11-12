import datetime
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from backend.models import Automation, Company



def indexView(request):
    data = Automation.objects.filter(status=True)

    context = {
        'data': data
    }

    return render(request, 'Automation/index.html', context)


def newView(request):

    companies = Company.objects.filter(status=True)

    context = {
        'companies': companies
    }
    return render(request, 'Automation/new.html', context)


@login_required
def SaveAction(request):

    if request.method == 'POST':
        company_id = request.POST.get('company_id', None)
        name = request.POST.get('name', None)
        short_name = request.POST.get('short_name', None)
        ip = request.POST.get('ip', None)
        subnet = request.POST.get('subnet', None)
        gateway = request.POST.get('gateway', None)
        mac = request.POST.get('mac', None)
        type_location = request.POST.get('type_location', 0)
        description = request.POST.get('description', None)
        status = request.POST.get('status', 0)

        if not company_id:
            messages.add_message(request, messages.ERROR, 'Empresa é obrigatório!')
            return redirect('AutomationNewAction')

        company = Company.objects.get(id=company_id)

        item = Automation()
        item.company = company
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
        item.created_at = datetime.datetime.now()
        item.save()

        messages.add_message(request, messages.SUCCESS, 'Registro salvo com sucesso!')

    return redirect('AutomationIndexView')


@login_required
def deleteAction(request, automation_id):

    item = Automation.objects.get(id=automation_id)
    item.delete()

    context = {
        'status': 200,
        'descricao': 'Excluído com sucesso'
    }

    return HttpResponse(json.dumps(context, ensure_ascii=False), content_type="application/json")
