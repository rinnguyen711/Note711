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


# class NoteViewSet2(viewsets.ModelViewSet, APIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     print("HELLO")
#     parser_classes = (FormParser, FileUploadParser)
#
#     def create(self, request):
#         data = request.data
#         print(data)
#         serializer = NoteSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#     def list(self, request):
#         serializer = NoteSerializer(self.queryset, many=True)
#         return Response(serializer)

#
# class NoteViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Note.objects.all()
#         serializer = NoteSerializer(queryset, many=True)
#         print(serializer.data)
#         return Response(serializer.data)

def index(request):
    return HttpResponse('HELLO')


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
        serializer = NoteSerializer(data=request.data)
        print("DATA:")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)





