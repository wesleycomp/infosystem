from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "public"

urlpatterns = [
    path('', views.FuncaoListView.as_view(), name='funcao_list'),
    path('funcao/edit/<int:pk>', views.FuncaoUpdateView.as_view(), name='funcao_edit'),
    path('funcao/<int:pk>/', views.FuncaoDetailView.as_view(), name='funcao_detail'),
    path('funcao/delete/<int:pk>', views.FuncaoDeleteView.as_view(), name='funcao_delete'),
    path('funcao/create', views.FuncaoCreateView.as_view(), name='funcao_create'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

