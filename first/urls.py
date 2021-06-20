from django.conf.urls import url
from django.urls import path
from first import views
from .views import index


urlpatterns = [
    path('', index, name='index'),
]
