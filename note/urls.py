from django.urls import path
from note import views
from .views import NoteViewSet

from rest_framework import routers

#urlpatterns = [
#    path('notes/', views.note_list),
#]

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, base_name='note')
urlpatterns = router.urls

