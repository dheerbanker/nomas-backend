from django.urls import path, include
from .views import NoteViewSet

urlpatterns = [
    path('all/', NoteViewSet.as_view({'get': 'list'})),
    path('create/', NoteViewSet.as_view({'post': 'create'})),
]