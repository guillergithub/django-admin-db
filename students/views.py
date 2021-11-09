from students.models import Student
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from students.serializers import StudentSerializer

# Create your views here.
class AllStudentsViewSet (ListCreateAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateUserViewSet (RetrieveUpdateDestroyAPIView):  
    queryset = Student.objects.all()
    serializer_class = StudentSerializer







