from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "public"

urlpatterns = [
    path('funcao', views.FuncaoListView.as_view(), name='funcao_list'),
    path('funcao/edit/<slug>', views.FuncaoUpdateView.as_view(), name='funcao_edit'),
    path('funcao/<slug>/', views.FuncaoDetailView.as_view(), name='funcao_detail'),
    path('funcao/delete/<slug>', views.FuncaoDeleteView.as_view(), name='funcao_delete'),
    path('funcao/create', views.FuncaoCreateView.as_view(), name='funcao_create'),

    path('empresa', views.EmpresaListView.as_view(), name='empresa_list'),
    path('empresa/edit/<slug>', views.EmpresaUpdateView.as_view(), name='empresa_edit'),
    path('empresa/<slug>/', views.EmpresaDetailView.as_view(), name='empresa_detail'),
    path('empresa/delete/<slug>', views.EmpresaDeleteView.as_view(), name='empresa_delete'),
    path('empresa/create', views.EmpresaCreateView.as_view(), name='empresa_create'),

    path('paciente', views.PacienteListView.as_view(), name='paciente_list'),
    path('paciente/edit/<slug>', views.PacienteUpdateView.as_view(), name='paciente_edit'),
    path('paciente/<slug>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    path('paciente/delete/<slug>', views.PacienteDeleteView.as_view(), name='paciente_delete'),
    path('paciente/create', views.PacienteCreateView.as_view(), name='paciente_create'),

    path('exame', views.ExameListView.as_view(), name='exame_list'),
    path('exame/edit/<slug>', views.ExameUpdateView.as_view(), name='exame_edit'),
    path('exame/<slug>/', views.ExameDetailView.as_view(), name='exame_detail'),
    path('exame/delete/<slug>', views.ExameDeleteView.as_view(), name='exame_delete'),
    path('exame/create', views.ExameCreateView.as_view(), name='exame_create'),

    path('especialidademedica', views.EspecialidadeMedicaListView.as_view(), name='especialidademedica_list'),
    path('especialidademedica/edit/<slug>', views.EspecialidadeMedicaUpdateView.as_view(), name='especialidademedica_edit'),
    path('especialidademedica/<slug>/', views.EspecialidadeMedicaDetailView.as_view(), name='especialidademedica_detail'),
    path('especialidademedica/delete/<slug>', views.EspecialidadeMedicaDeleteView.as_view(), name='especialidademedica_delete'),
    path('especialidademedica/create', views.EspecialidadeMedicaCreateView.as_view(), name='especialidademedica_create'),

    path('prestadorservico', views.PrestadorServicoListView.as_view(), name='prestadorservico_list'),
    path('prestadorservico/edit/<slug>', views.PrestadorServicoUpdateView.as_view(), name='prestadorservico_edit'),
    path('prestadorservico/<slug>/', views.PrestadorServicoDetailView.as_view(), name='prestadorservico_detail'),
    path('prestadorservico/delete/<slug>', views.PrestadorServicoDeleteView.as_view(), name='prestadorservico_delete'),
    path('prestadorservico/create', views.PrestadorServicoCreateView.as_view(), name='prestadorservico_create'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

