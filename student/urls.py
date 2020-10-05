from django.urls import path
from .views import *

app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
    path('enroll/', enroll, name='enroll'),
    path('update/<int:student_id>/', update, name='update'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
    path('<int:student_id>/fees/payment/', pay_fees, name='pay_fees'),
]