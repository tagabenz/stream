from django.contrib import admin
from django.urls import path

from homepage import views as index
from blog import views as blog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.Index.as_view()),
    path('blog/', blog.Index.as_view())
]
