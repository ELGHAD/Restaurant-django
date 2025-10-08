from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MenuItem

def home(request):
    return render(request, 'restaurant/home.html')

def about(request):
    return render(request, 'restaurant/about.html')

def book(request):
    return render(request, 'restaurant/book.html')

class MenuListView(ListView):
    model = MenuItem
    template_name = 'restaurant/menu.html'
    context_object_name = 'items'  # uses model Meta.ordering

class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'restaurant/menu_item.html'
    context_object_name = 'item'
