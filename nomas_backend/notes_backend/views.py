import datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


#for some reason DELETE button is shown in all methods, altho it doesn't work (gives error) due to lack of id / object.
# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    """API endpoints related to the Note model"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

              #**FILTERING**
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'title']


    # GET method
    def list(self, request):
        """List all notes"""
        notes = list(self.get_queryset())
        serializer = NoteSerializer(notes, many=True)
        # json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


    def retrieve(self,request, id):
       notes= Note.objects.filter(id=id)  
       serializer = NoteSerializer(notes, many=True)
       return Response(serializer.data)


    # POST method
    def create(self, request):
    
      serializer = NoteSerializer(data=request.data)
      
      if serializer.is_valid():   
            model = Note(**serializer.data)
            model.save()
            return Response({'Message': 'Voila! Note created successfully'}, status=201)
      else:
          return Response({'Error': "Missing fields. Must include 'title'"}, status=400)


    #DELETE method
    #page will still load even if note id doesn't exist; will only show error when you press DELETE
    def delete(self, request, id):
        #checks for valid ids
        notes = list(self.get_queryset())
        if not any(n.id == id for n in notes):
            return Response({'message': "Whoa! Note doesn't exist, buddy"}, status=404)
        
        note = Note.objects.get(id=id)
        note.delete()
        return Response({'Message': "Note deleted successfully"}, status=200)


    #PUT method
    #page will still load even if  note id doesn't exist; will only show error when you press PUT.  
    def update(self, request, id):
        #checks for valid ids
        notes = list(self.get_queryset())
        if not any(n.id == id for n in notes):
            return Response({'message': "Whoa! Note doesn't exist, buddy"}, status=404)
        
        note = Note.objects.get(id=id)
        data1 = NoteSerializer(instance=note, data=request.data)
    
        if data1.is_valid():
            data1.save()
            return Response({'Message':"Note Updated!"}, status=201)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

