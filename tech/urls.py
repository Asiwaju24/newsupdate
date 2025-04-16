
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from news.views import home  

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('news/', include('news.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('', home, name='home'),
    path('ckeditor/', include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



