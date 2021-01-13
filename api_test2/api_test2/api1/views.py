import django_filters
from rest_framework import viewsets, filters
from .models import Todo
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
