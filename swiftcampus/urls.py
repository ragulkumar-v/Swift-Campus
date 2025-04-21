from django.contrib import admin
from django.urls import path, include
from portal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("portal.urls")),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
