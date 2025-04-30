from django.urls import path
from app.views import my_world
urlpatterns = [
   path('my_world/',my_world, name = 'my_world'),
]
