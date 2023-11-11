from django.urls import path, include

urlpatterns = [
    path('', include('backend.Routes.Login.urls')),
    path('automation/', include('backend.Routes.Automation.urls')),
    path('login/', include('backend.Routes.Login.urls')),
    path('dashboard/', include('backend.Routes.Dashboard.urls')),
    path('company/', include('backend.Routes.Company.urls')),
]
