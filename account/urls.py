from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('<int:student_id>/student/', index, name='index'),
    path('<int:account_id>/transactions/', get_transactions, name='transactions'),
    path('<int:transaction_id>/transaction/', generate_pdf, name='generate')
]