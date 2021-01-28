from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import *
from django.db.models import Q


class FuncaoListView(ListView):
    model = Funcao
    template_name = 'funcao/funcao_list.html'
    context_object_name = "funcoes"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        if query:
            object_list = Funcao.objects.filter(
                Q(nome_funcao__icontains=query) | Q(cbo__icontains=query)
            )
        else:
            object_list = Funcao.objects.all()
        return object_list

class FuncaoDetailView(DetailView):
    model = Funcao
    template_name = 'funcao/detail.html'

class FuncaoCreateView(SuccessMessageMixin, CreateView):
    form_class = FuncaoForm
    template_name = 'funcao/create.html'
    success_url = reverse_lazy('public:funcao_create')
    success_message = "Função cadastrada com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuariocadastro = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class FuncaoUpdateView(SuccessMessageMixin, UpdateView):
    model = Funcao
    form_class = FuncaoForm
    template_name = 'funcao/edit.html'
    success_url = reverse_lazy('public:funcao_list')
    success_message = "Função Editada com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuarioedicao = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class FuncaoDeleteView(SuccessMessageMixin, DeleteView):
    model = Funcao
    template_name = 'funcao/delete.html'
    success_url = reverse_lazy('public:funcao_list')
    success_message = "A função %s foi apagada com sucesso!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        messages.success(self.request, self.success_message % obj.nome_funcao) #obs: antes era obj.__dict__ impria o objeto inteiro
        return super(FuncaoDeleteView, self).delete(request, *args, **kwargs)


################################################## EMPRESA ####################################################
class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa/empresa_list.html'
    context_object_name = "empresas"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        if query:
            object_list = Empresa.objects.filter(
                Q(nome_empresa__icontains=query) | Q(cnpj__icontains=query)
            )
        else:
            object_list = Empresa.objects.all()
        return object_list

class EmpresaCreateView(SuccessMessageMixin, CreateView):
    form_class = EmpresaForm
    template_name = 'empresa/create.html'
    success_url = reverse_lazy('public:empresa_create')
    success_message = "Empresa cadastrada com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuariocadastro = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresa/detail.html'


class EmpresaUpdateView(SuccessMessageMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/edit.html'
    success_url = reverse_lazy('public:empresa_list')
    success_message = "Empresa Editada com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuarioedicao = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EmpresaDeleteView(SuccessMessageMixin, DeleteView):
    model = Empresa
    template_name = 'empresa/delete.html'
    success_url = reverse_lazy('public:empresa_list')
    success_message = "A Empresa %s foi apagada com sucesso!"

    def delete(self, request, *args, **kwargs):

        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.nome_empresa) #obs: antes era obj.__dict__ impria o objeto inteiro
        return super(EmpresaDeleteView, self).delete(request, *args, **kwargs)





################################################## PACIENTE ####################################################
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'
    context_object_name = "pacientes"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        if query:
            object_list = Paciente.objects.filter(
                Q(nome_paciente__icontains=query) | Q(cpf__icontains=query)
            )
        else:
            object_list = Paciente.objects.all()
        return object_list

class PacienteCreateView(SuccessMessageMixin, CreateView):
    form_class = PacienteForm
    template_name = 'paciente/create.html'
    success_url = reverse_lazy('public:paciente_create')
    success_message = "Paciente cadastrado com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuariocadastro = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente/detail.html'


class PacienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/edit.html'
    success_url = reverse_lazy('public:paciente_list')
    success_message = "Paciente Editado com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuarioedicao = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PacienteDeleteView(SuccessMessageMixin, DeleteView):
    model = Paciente
    template_name = 'paciente/delete.html'
    success_url = reverse_lazy('public:paciente_list')
    success_message ="O Paciente %s foi apagada com sucesso!"

    def delete(self, request, *args, **kwargs):

        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.nome_paciente) #obs: antes era obj.__dict__ impria o objeto inteiro
        return super(PacienteDeleteView, self).delete(request, *args, **kwargs)



################################################## exame ####################################################
class ExameListView(ListView):
    model = Exame
    template_name = 'exame/exame_list.html'
    context_object_name = "exames"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        if query:
            object_list = Exame.objects.filter(
                Q(nome_exame__icontains=query)
            )
        else:
            object_list = Exame.objects.all()
        return object_list

class ExameCreateView(SuccessMessageMixin, CreateView):
    form_class = ExameForm
    template_name = 'exame/create.html'
    success_url = reverse_lazy('public:exame_create')
    success_message = "Exame cadastrado com sucesso!"


  #  def moeda(valor):
   #     print(valor)
     #   valor = valor.replace('.', '')
     #   valor = valor.replace(',', '.')
     #   return Decimal(valor)
    #    return valor

    def form_valid(self, form):
     #   print('aki 2')



       # self.valor_colaborador = 6.0
       #self.valor_ems = 12.00
        self.object = form.save(commit=False)

       # print(self.object.valor_colaborador)
      #  self.object.valor_exame = ExameCreateView.moeda(self.object.valor_colaborador)

        self.object.idusuariocadastro = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ExameDetailView(DetailView):
    model = Exame
    template_name = 'exame/detail.html'


class ExameUpdateView(SuccessMessageMixin, UpdateView):
    model = Exame
    form_class = ExameForm
    template_name = 'exame/edit.html'
    success_url = reverse_lazy('public:exame_list')
    success_message = "Exame Editado com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuarioedicao = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ExameDeleteView(SuccessMessageMixin, DeleteView):
    model = Exame
    template_name = 'exame/delete.html'
    success_url = reverse_lazy('public:exame_list')
    success_message ="O Exame %s foi apagada com sucesso!"

    def delete(self, request, *args, **kwargs):

        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.nome_exame) #obs: antes era obj.__dict__ impria o objeto inteiro
        return super(PacienteDeleteView, self).delete(request, *args, **kwargs)


################################################## ESPECIALIDADE MEDICA ####################################################
class EspecialidadeMedicaListView(ListView):
    model = EspecialidadeMedica
    template_name = 'especialidademedica/especialidademedica_list.html'
    context_object_name = "especialidademedicas"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        if query:
            object_list = EspecialidadeMedica.objects.filter(
                Q(especialidade_medica__icontains=query)
            )
        else:
            object_list = EspecialidadeMedica.objects.all()
        return object_list

class EspecialidadeMedicaCreateView(SuccessMessageMixin, CreateView):
    form_class = EspecialiadeMedicaForm
    template_name = 'especialidademedica/create.html'
    success_url = reverse_lazy('public:especialidademedica_create')
    success_message = "Especialidade Medica cadastrado com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuariocadastro = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EspecialidadeMedicaDetailView(DetailView):
    model = EspecialidadeMedica
    template_name = 'especialidademedica/detail.html'


class EspecialidadeMedicaUpdateView(SuccessMessageMixin, UpdateView):
    model = EspecialidadeMedica
    form_class = EspecialiadeMedicaForm
    template_name = 'especialidademedica/edit.html'
    success_url = reverse_lazy('public:especialidademedica_list')
    success_message = "Especialidade Medica Editado com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuarioedicao = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EspecialidadeMedicaDeleteView(SuccessMessageMixin, DeleteView):
    model = EspecialidadeMedica
    template_name = 'especialidademedica/delete.html'
    success_url = reverse_lazy('public:especialidademedica_list')
    success_message ="A Especialidade Medica %s foi apagada com sucesso!"

    def delete(self, request, *args, **kwargs):

        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.especialidade_medica) #obs: antes era obj.__dict__ impria o objeto inteiro
        return super(EspecialidadeMedicaDeleteView, self).delete(request, *args, **kwargs)





################################################## PRESTADOR DE SERVIÇO ####################################################
class PrestadorServicoListView(ListView):
    model = PrestadorServico
    template_name = 'prestadorservico/prestadorservico_list.html'
    context_object_name = "prestadorservicos"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        if query:
            object_list = PrestadorServico.objects.filter(
                Q(nome_prestador__icontains=query)
            )
        else:
            object_list = PrestadorServico.objects.all()
        return object_list

class PrestadorServicoCreateView(SuccessMessageMixin, CreateView):
    form_class = PrestadorServicoForm
    template_name = 'prestadorservico/create.html'
    success_url = reverse_lazy('public:prestadorservico_create')
    success_message = "Prestador Serviço cadastrado com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuariocadastro = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PrestadorServicoDetailView(DetailView):
    model = PrestadorServico
    template_name = 'prestadorservico/detail.html'


class PrestadorServicoUpdateView(SuccessMessageMixin, UpdateView):
    model = PrestadorServico
    form_class = PrestadorServicoForm
    template_name = 'prestadorservico/edit.html'
    success_url = reverse_lazy('public:prestadorservico_list')
    success_message = "Prestador de Serviço Editado com sucesso!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.idusuarioedicao = self.request.user.id
        messages.success(self.request, self.success_message)  # obs: antes era obj.__dict__ impria o objeto inteiro
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PrestadorServicoDeleteView(SuccessMessageMixin, DeleteView):
    model = PrestadorServico
    template_name = 'prestadorservico/delete.html'
    success_url = reverse_lazy('public:prestadorservico_list')
    success_message ="O Prestador de Serviço %s foi apagado com sucesso!"

    def delete(self, request, *args, **kwargs):

        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.nome_prestador) #obs: antes era obj.__dict__ impria o objeto inteiro
        return super(PrestadorServicoDeleteView, self).delete(request, *args, **kwargs)
