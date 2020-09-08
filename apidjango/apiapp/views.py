from django.shortcuts import render
from  django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Form
from .serializers import FormSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class FormViewSet(viewsets.ModelViewSet):
    queryset=Form.objects.all()
    serializer_class=FormSerializer

# @api_view(['GET','POST'])
# def form_list(request):
#     if request.method=='GET':
#         alldata=Form.objects.all()
#         serializer=FormSerializer(alldata,many=True)
#         return Response(serializer.data)
    
#     elif request.method=='POST':
#         serializer=FormSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
