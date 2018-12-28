from django.contrib import admin
from django.urls import path, include
from surat_menyurat import views
# from inventaris import views as inven_views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('home/', views.home, name='home'),    
    path('surat/', include('surat_menyurat.urls', namespace="surat")),
    path('inventaris/', include('inventaris.urls', namespace="inventaris_itec")),#include('inventaris.urls', namespace='inventaris')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
