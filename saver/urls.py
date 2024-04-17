from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.viewitem, name='viewitem'),
    path('delete/<item_id>/', views.deleteitem, name='deleteitem'),
    path('details/<item_id>/', views.viewitemdetails, name='viewitemdetails'),
]