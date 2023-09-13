from django.urls import path
from backend.Controller import CompanyController as cc

urlpatterns = [
    path('new', cc.newView, name="CompanyNewAction"),
    path('save', cc.SaveAction, name="CompanySaveAction")
]
