from django.shortcuts import render
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from mainblog import *
from rest_framework import status
# Create your views here.


@api_view(["GET"])
def postview(request):
    datasets=Post.objects.all()
    selializers=Postserilazers(datasets,many=True)
    return Response(selializers.data)
