from rest_framework import serializers
from mainblog.models import *

class Postserilazers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields= '__all__'
