from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# API v1
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Models and serializers
from .models import Reading
from .serializers import ReadingSerializer


def index(request):
    return HttpResponse('tracker index works!')


@api_view(['GET', 'POST'])
def reading_list(request, format=None):
    if request.method == 'GET':
        readings = Reading.objects.all()
        serializer = ReadingSerializer(readings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reading_detail(request, pk, format=None):
    try:
        reading = Reading.objects.get(pk=pk)
    except Reading.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReadingSerializer(reading)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReadingSerializer(reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def reading_list_v1(request):
    if request.method == 'GET':
        readings = Reading.objects.all()
        serializer = ReadingSerializer(readings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReadingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def reading_detail_v1(request, pk):
    try:
        reading = Reading.objects.get(pk=pk)
    except Reading.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReadingSerializer(reading)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReadingSerializer(reading, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        reading.delete()
        return HttpResponse(status=204)
