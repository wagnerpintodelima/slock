from django.urls import path
from backend.Controller import CompanyController as cc

urlpatterns = [
    path('', cc.indexView, name="CompanyIndexView"),
    path('new', cc.newView, name="CompanyNewView"),
    path('save', cc.saveAction, name="CompanySaveAction"),
    path('delete/<int:company_id>', cc.deleteAction, name="CompanyDeleteAction"),
]
