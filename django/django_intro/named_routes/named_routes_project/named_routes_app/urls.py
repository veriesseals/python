from django.urls import path
from . import views

urlpatterns = [
    path('', views.toindex, name='my_index'),
    path('this_app/new', views.new, name='my_new'),
    path('this_app/<int:id>/edit', views.edit, name='my_edit'),
    path('this_app/<int:id>/delete', views.delete, name='my_delete'),
    path('this_app/<int:id>', views.shows, name='my_show'),
]