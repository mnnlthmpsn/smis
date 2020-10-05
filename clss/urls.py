from django.urls import path
from .views import *

app_name = 'class'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('update/<int:class_id>/', update, name='update'),
    path('delete/<int:class_id>/', delete, name='delete'),
]