from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',include('api.urls')),
    path('blog/',include('blog.urls')),
    path('account/',include('account.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)