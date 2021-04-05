from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('<int:student_id>/student/', index, name='index'),
    path('<int:account_id>/transactions/', get_transactions, name='transactions'),
    path('<int:pk>/transaction/', render_pdf_view, name='generate')
]