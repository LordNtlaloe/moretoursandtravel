from django.shortcuts import render
from rest_framework import viewsets
from . models import Visitor
from . serializers import VisitorSerializer

# Create your views here.
class VisitorViewset(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer