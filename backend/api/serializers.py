from rest_framework import serializers
from .models import Visitor

class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitor
        fields = ['first_name', 'last_name']