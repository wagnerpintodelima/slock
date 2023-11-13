from django.urls import path
from backend.Controller import AutomationController as ac

urlpatterns = [
    path('', ac.indexView, name="AutomationIndexView"),
    path('new', ac.newView, name="AutomationNewAction"),
    path('save', ac.SaveAction, name="AutomationSaveAction"),
    path('edit/<int:automation_id>', ac.editView, name="AutomationEditView"),
    path('edit/save', ac.editAction, name="AutomationEditAction"),
    path('delete/<int:automation_id>', ac.deleteAction, name="AutomationDeleteAction"),
]
