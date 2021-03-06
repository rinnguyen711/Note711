from .models import Note
from .serializers import NoteSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from NoteServer import settings
import requests

@csrf_exempt
def note_list(request):

    if request.method == 'GET':
        note = Note.objects.all()
        serializer = NoteSerializer(note, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def index(request):
    db = settings.DATABASES['default']
    host = request.get_host()
    
    
    return HttpResponse(db['NAME'] + '\n\r Go to: <a href="'+ host + '/api/' +'">API</a>')


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @action(methods=['get'], detail=False)
    def first(self, request):
        first = self.get_queryset().order_by('title').last()
        serializer = NoteSerializer(first)
        print(serializer.data)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def new(self, request):
        
        data = request.data
        
        note = Note()
        note.title = data['title']
        note.msg = data['msg']
        note.image = data['image']
        note.save()
        
        image = data['image']
        files = {'image': open(note.image.path, 'rb')}
        response = requests.post(url='http://rinnguyen.pythonanywhere.com/api/faces/new/', files=files)
        content = response.content
        
        
        return Response(content)





