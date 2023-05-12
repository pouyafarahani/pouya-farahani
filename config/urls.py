from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),
                  path('blog/', include('blog.urls')),
                  path('about/', include('about.urls')),
                  path('__debug__/', include('debug_toolbar.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
