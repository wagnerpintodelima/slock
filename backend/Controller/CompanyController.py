from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from backend.Controller.BaseController import saveFile
from backend.models import Company

_PATH_FILE_COMPANY = 'backend/upload/company/'

def newView(request):
    context = {}
    return render(request, 'Company/new.html', context)



@login_required
def SaveAction(request):

    if request.method == 'POST':
        razaoSocial = request.POST.get('razaoSocial', None)
        nomeFantasia = request.POST.get('nomeFantasia', None)
        email = request.POST.get('email', None)
        cnpj = request.POST.get('cnpj', None)
        telefone = request.POST.get('telefone', None)
        cep = request.POST.get('cep', None)
        uf = request.POST.get('uf', 0)
        bairro = request.POST.get('bairro', None)
        rua = request.POST.get('rua', None)
        numero = request.POST.get('numero', None)
        cidade = request.POST.get('cidade', None)
        observacao = request.POST.get('observacao', None)
        logo = request.FILES['logo']
        banner = request.FILES['banner']
        status = request.POST.get('status', 0)

        item = Company()
        item.razao_social = razaoSocial
        item.nome_fantasia = nomeFantasia
        item.email = email
        item.cpf_cnpj = cnpj
        item.phone_number = telefone
        item.cep = cep
        item.uf = uf
        item.neighborhood = bairro
        item.street = rua
        item.house_number = numero
        item.city = cidade
        item.observation = observacao
        if logo:
            item.logo = saveFile(_PATH_FILE_COMPANY, 'png', logo)
        if banner:
            item.picture = saveFile(_PATH_FILE_COMPANY, 'png', banner)
        item.status = status
        item.save()

        messages.add_message(request, messages.SUCCESS, 'Registro salvo com sucesso!')

    return redirect('CompanyNewAction')