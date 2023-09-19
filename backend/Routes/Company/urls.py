from django.urls import path
from backend.Controller import CompanyController as cc

urlpatterns = [
    path('', cc.indexView, name="CompanyIndexView"),
    path('new', cc.newView, name="CompanyNewView"),
    path('save', cc.saveAction, name="CompanySaveAction"),
    path('edit/<int:company_id>', cc.editView, name="CompanyEditView"),
    path('edit/save/<int:company_id>', cc.editAction, name="CompanyEditAction"),
    path('delete/<int:company_id>', cc.deleteAction, name="CompanyDeleteAction"),
]
