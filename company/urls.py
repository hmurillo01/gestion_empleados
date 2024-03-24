from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name="inicio"),
    path('salary/', views.salary, name="salary"),
    path('save/', views.save, name = "save"),
    path('job/', views.job,name= "job"),
    path('savejob/',views.savejob,name="savejob"),
    path('lista_salarios/',views.lista_salarios,name="lista_salarios"),
    path('listar_job/', views.listar_job, name='listar_job'),
    path('buscar_trabajo/', views.buscar_trabajo, name='buscar_trabajo'),
]