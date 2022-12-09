from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_system.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
