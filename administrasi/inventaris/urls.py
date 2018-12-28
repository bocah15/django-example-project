from django.urls import path, include
from . import views

app_name = 'inventaris'

urlpatterns = [
	path('inventaris-list', views.InventarisListView.as_view(), name='inventaris_list'),
	path('inventaris-form', views.InventarisCreateView.as_view(), name='inventaris_form'),
	path('inventaris-delete/<int:id>', views.InventarisDeleteView.as_view(), name='inventaris_delete'),
	path('inventaris-edit/<int:pk>', views.InventarisUpdateView.as_view(), name='inventaris_edit'),
]