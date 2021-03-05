from django.shortcuts import render
from rest_framework import viewsets

from .models import File
from .serializers import FileSerializer


class FlieViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
