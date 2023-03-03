from django.test import TestCase, Client
from rest_framework.test import APIClient
from .views import NoteViewSet
from django.urls import reverse
from .models import Note
import json
from .serializers import NoteSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
# Create your tests here.
class Testviews(TestCase):

    def setUp(self):
        # client= APIClient()
        self.Note1 = Note.objects.create(
            id=24,
            title= "test 1",
            content= "test content"
        )

    def test_Note_list_GET(self):
        response= self.client.get(reverse('list'))

        self.assertEquals(response.status_code, 200) 

    def test_Note_create_POST(self):
        response= self.client.post(reverse('create'), {'title':"test 1", 'content':"test content"})
        self.assertEqual(response.status_code, 201)
        #print(response.content)
        # print(response)
        # serializer = NoteSerializer(data=response)
        # print(serializer)
        # serializer.is_valid()
        # self.assertEquals(response.status_code, 201)
        # self.assertEquals(response, self.Note1)
        # print(response.get(dict(serializer)))

    def test_Note_retrieve_GET(self):

        response= self.client.get(reverse('retrieve', args=[24]))
        #print(response.content)
        notereq = Note.objects.filter(id=24)
        note=NoteSerializer(notereq, many=True)
        json= JSONRenderer().render(note.data)
        #print(json)
        self.assertEqual(json, response.content)

    def test_Note_delete_DELETE(self):
        response = self.client.delete(reverse('delete', args=[24]))
        # print(response.status_code)
       
        if Note.objects.filter(id=24).exists():
          raise FileExistsError
        else:
            pass
    
    def test_Note_update_PUT(self):
        response= self.client.put(reverse('update', args=[24]), data={'title':"New test", 'content':"New test content"}, content_type='application/json')
        #print(response.status_code)
        self.assertEquals(response.status_code, 201)