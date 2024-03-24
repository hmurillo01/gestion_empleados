from django.shortcuts import render
from django.http import HttpResponse
from .models import Salary,Job
from django.db.models import Q
# Create your views here.
def index(request):

  return render(request, 'index.html', {})

def salary(request):
  return render(request, "salario.html", {})

def save(request):
  amount = request.GET['amount']
  salary = Salary(amount = amount)
  salary.save()
  print(amount)
  return HttpResponse("Hola")

def job (request):
  #listamos los salarios 
  salary=Salary.objects.all()
  return render(request,'trabajo.html',{
    "salary":salary
  })

def savejob(request):
  
  name=request.POST['name']
  description= request.POST['description']
  salary = Salary.objects.get(id=request.POST['salary'])
  job= Job (name=name, description=description, salary=salary)
  job.save()
  
  return HttpResponse ("Puesto de trabajo creado")

def lista_salarios(request):
    salaries = Salary.objects.all()  # Recupera todos los objetos de salario
    return render(request, "lista_salarios.html", {'salary': salaries})
  


def listar_job(request):
    # Obtener todos los trabajos y sus salarios asociados
    jobs = Job.objects.all()
    return render(request, 'listar_job.html', {'jobs': jobs})
  


def buscar_trabajo(request):
    query = request.GET.get('q')
    jobs = None
    if query:
        # Realizar la búsqueda en los trabajos por nombre o descripción
        jobs = Job.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'buscar_trabajo.html', {'jobs': jobs})
  
  





