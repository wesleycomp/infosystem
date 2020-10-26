from django.conf.urls import url
from . import views

app_name = "public"

urlpatterns = [
    url("func", views.FuncaoListView.as_view(), name='funcao'),
]
