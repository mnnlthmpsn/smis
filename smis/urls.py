from django.contrib import admin
from django.urls import path, include

# views
from staff.views import index, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('account/', include('account.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('class/', include('clss.urls')),
    path('staff/', include('staff.urls')),
    path('student/', include('student.urls')),
]
