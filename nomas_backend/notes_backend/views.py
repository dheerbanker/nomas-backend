import datetime
from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response

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