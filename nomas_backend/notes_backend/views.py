import datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response

#for some reason DELETE button is shown in all methods, altho it doesn't work (gives error) due to lack of id / object.
# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    """API endpoints related to the Note model"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    
    # GET method
    def list(self, request):
        """List all notes"""
        notes = list(self.get_queryset())
        result = []
        for note in notes:
            result.append(dict(
                id = note.id,
                title = note.title,
                content = note.content,
                created_at = note.created_at,
                last_modified = note.last_modified,
            ))

        return Response(result)

    # POST method
    def create(self, request):
        if not all(x in request.data for x in ['title', 'content']):
            return Response({'error': "Missing fields. Must include 'title', 'content'."}, status=400)

        note_creation_data = dict(
            title = request.data['title'],
            content = request.data['content'],
        )

        model = Note(**note_creation_data)

        model.save()

        return Response({'message': "Voila! Note created successfully"}, status=201)

    #DELETE method
    #page will still load even if note id doesn't exist; will only show error when you press DELETE
    def delete(self, request, id):
        #checks for valid ids
        notes = list(self.get_queryset())
        if not any(n.id == id for n in notes):
            return Response({'message': "Whoa! Note doesn't exist, buddy"}, status=404)

        note = Note.objects.get(id=id)
        note.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


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
            return Response(data1.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

