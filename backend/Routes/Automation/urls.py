from django.urls import path
from backend.Controller import AutomationController as ac

urlpatterns = [
    path('', ac.indexView, name="AutomationIndexView"),
    path('new', ac.newView, name="AutomationNewAction"),
    path('save', ac.SaveAction, name="AutomationSaveAction"),
    path('delete/<int:automation_id>', ac.deleteAction, name="AutomationDeleteAction"),
]
