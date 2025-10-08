# C:\Users\lenovo\littlelemon\restaurant\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('menu/', views.MenuListView.as_view(), name='menu'),
    path('menu_item/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu_item'),
]
