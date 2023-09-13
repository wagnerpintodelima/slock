from django.urls import path
from backend.Controller import AutomationController as ac

urlpatterns = [
    path('new', ac.newView, name="AutomationNewAction"),
    path('save', ac.SaveAction, name="AutomationSaveAction")
]
