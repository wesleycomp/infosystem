from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *


class FuncaoListView(ListView):
    model = Funcao
    template_name ='funcao/list.html'

class ContactDetailView(DetailView):
    model = Funcao

class ContactCreateView(CreateView):
    model = Funcao

class ContactUpdateView(UpdateView):
    model = Funcao

class ContactDeleteView(DeleteView):
    model = Funcao

