from django.shortcuts import render
from students.models import Student

# Create your views here.
def studentsList(request):
  list = Student.objects.all()
  context = { 'students': list }
  if (request.method == 'POST'):
    try:
      Student.objects.create(nombre=request.POST['nombre'], edad=request.POST['edad'], correo=request.POST['correo'])
      print('El estudiante se ha creado satisfactoriamente')
    except:
      print('Error al crear un usuario')    
      
    print(list)
    return render(request, 'students/list.html', context)

def studentDetail(request, id): 
  student = Student.objects.get(id=id)
  context = { 'student': student }
  print(student)
  return render(request, 'students/detail.html', context)
