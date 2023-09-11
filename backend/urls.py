from django.urls import path, include

urlpatterns = [
    path('automation/', include('backend.Routes.Automation.urls')),
    path('login/', include('backend.Routes.Login.urls')),
    path('dashboard/', include('backend.Routes.Dashboard.urls')),
]
