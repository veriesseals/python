from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_generator),
    path('word_generator', views.word_generator),
    path('reset', views.reset)
]