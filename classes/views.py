from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from classes.models import Classes
from classes.serializers import ClassesSerializer


class AllClassesViewSet(ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class UpdateClassViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer