from django.shortcuts import render
from .models import Movie,Guest,Reservation
from django.http import JsonResponse
import json
from .serializers import MovieSerializer,GuestSerializer,ReservationSerializer
from rest_framework import filters,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

#Views
#1 without Rest no model query
def no_rest_no_model(request):
    guests=[
        {
            'id':1, "name":'ahmed' , "mobile":"8987868"
        },
        {
            'id':2 , "name":'karim' , "mobile":"098867"
        }         
    ]
    return JsonResponse(guests,safe=False)

#2 no REST from model
def no_rest_from_model(request):
    data=Guest.objects.all()
    response={
        'guests':list(data.values('name','mobile','reservation'))
    }
    return JsonResponse(response)

#3.1 Function based view  with REST  GET POST
@api_view(['GET','POST'])
def FBV_list(request):
    #GET
    if request.method=='GET':
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    #POST
    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data)
        # return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
#page has just a json format
@api_view(['GET'])
def fbv_list_just_json(request):
    if request.method=='GET':
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return JsonResponse(serializer.data, safe=False)      
#3.2 Get PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk):
    try:
        guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method=='GET':
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    if request.method=='PUT':
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method=='DELETE':
        guest.delete()
        return Response(stattus=status.HTTP_204_NO_CONTENT)
    
    
def display_data(request):
    response=requests.get('https://api.covid19api.com/countries').json()
    return render(request,'display_data.html',{'response':response})
    
def data_flespi(request):
    # Flespi API request
    url = 'https://flespi.io/api/1'
    headers = {
        'Authorization': 'FlespiToken <H1H3i1hh6OJswF2WQV8tVNOMlVO2UHqsxWjFNqMH2lXoOQ9sz7KkIoUT7zMR407p>'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    # Render template
    return render(request, 'flespi_data.html', {'data': data})
    



# def json_format(request):
#     data=list(JsonFormat.objects.exclude(id=1).order_by().values())
#     return JsonResponse(data,safe=False)

