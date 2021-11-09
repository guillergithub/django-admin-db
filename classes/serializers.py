from rest_framework.serializers import ModelSerializer
from classes.models import Classes

class ClassesSerializer(ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

