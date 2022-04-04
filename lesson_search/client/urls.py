from django.urls import path
from . import views

urlpatterns = [
    path('generate/<int:count>/', views.generate, name='generate'),
    path('', views.ClientView.as_view(), name='client_list'),
    path('products/', views.ProductView.as_view(), name='product_list'),
    path('search/', views.search, name='search'),
    path('test/', views.test_list_view, name='test'),


]
