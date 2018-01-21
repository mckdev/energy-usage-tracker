from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Reading
from .serializers import ReadingSerializer


def index(request):
	return HttpResponse('tracker index works!')


@csrf_exempt
def reading_list(request):
    if request.method == 'GET':
        readings = Reading.objects.all()
        serializer = ReadingSerializer(readings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def reading_detail(request, pk):
    try:
        reading = Reading.objects.get(pk=pk)
    except Reading.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReadingSerializer(reading)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(reading, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        reading.delete()
        return HttpResponse(status=204)
