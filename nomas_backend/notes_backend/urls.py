from django.urls import path, include
from .views import NoteViewSet

urlpatterns = [
    path('all/', NoteViewSet.as_view({'get': 'list'}), name="list"),
    path('create/', NoteViewSet.as_view({'post': 'create'}), name='create'),
    path('delete/<int:id>', NoteViewSet.as_view({'delete': 'delete'}), name='delete'),
    path('update/<int:id>', NoteViewSet.as_view({'put': 'update'}), name='update'),
    path('retrieve/<int:id>', NoteViewSet.as_view({'get': 'retrieve'}), name='retrieve'),
    
]
