from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from stream_app import settings
from homepage.views import pageNotFound
from studio.views import StudioAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_users.urls')),
    path('', include('blog.urls')),
    path('', include('studio.urls')),
    path('', include('homepage.urls')),
    path('api/v1/studio/<slug:command>', StudioAPIView.as_view(),name="is_online"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

 