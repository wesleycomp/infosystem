from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import *



class FuncaoListView(ListView):
    model = Funcao
    template_name = 'funcao/funcao_list.html'
    context_object_name = "funcoes"
    paginate_by = 4


class FuncaoDetailView(DetailView):
    model = Funcao
    template_name = 'funcao/detail.html'
   # context_object_name = 'funcao'

class FuncaoCreateView(SuccessMessageMixin, CreateView):
    form_class = FuncaoForm
    template_name = 'funcao/create.html'
    success_url = reverse_lazy('public:funcao_create')
    success_message = "Função cadastrada com sucesso!"

class FuncaoUpdateView(SuccessMessageMixin, UpdateView):
    model = Funcao
    form_class = FuncaoForm
    template_name = 'funcao/edit.html'
    success_url = reverse_lazy('public:funcao_list')
    success_message = "Função Editada com sucesso!"


class FuncaoDeleteView(SuccessMessageMixin, DeleteView):
    model = Funcao
    template_name = 'funcao/delete.html'
    success_url = reverse_lazy('public:funcao_list')
    success_message = "A função %s foi apagada com sucesso!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.descricao) #obs: antes era obj.__dict__ impria o objeto inteiro
        return super(FuncaoDeleteView, self).delete(request, *args, **kwargs)
