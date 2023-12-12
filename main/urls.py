from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path("modified/", include('modified.urls')),
    path('note/', include('note.urls'))
]
