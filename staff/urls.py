from django.urls import path
from .views import *

app_name = 'staff'

urlpatterns = [
    path('', view, name='index'),
    path('add/', add, name='add'),
    path('update/<int:staff_id>/', update, name='update'),
    path('delete/<int:staff_id>/', delete, name='delete'),
]