from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# views
from staff.views import index, dashboard, error_404, error_505

urlpatterns = [
    path('', index, name='index'),
    path('account/', include('account.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('class/', include('clss.urls')),
    path('staff/', include('staff.urls')),
    path('student/', include('student.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = error_404
handler404 = error_505