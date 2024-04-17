from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
class CarView(APIView):
    def get(self, request):
        result = Car.objects.all()
        carserializer = CarSerializer(result, many=True)
        return Response(carserializer.data)
    
    def post(self, request):
        data = request.data
        carserializer = CarSerializer(data=data)
        if carserializer.is_valid():
            carserializer.save()
            return Response(carserializer.data, status=status.HTTP_201_CREATED)
        return Response(carserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CarDetail(APIView):
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
  
    def get(self, request, format=None):
        pk = request.data.get('pk')
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
  
    def put(self, request, format=None):
        pk = request.data.pk
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, format=None):
        pk = request.data.pk
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, format=None):
        pk = request.data.pk
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)