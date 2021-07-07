from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from images import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('/upload', views.homeUpload, name='homeUpload'),
    path('delete/<image_id>', views.delete, name='delete'),
    path('download/<image_id>', views.download, name='download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)