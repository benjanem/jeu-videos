import django
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# Images & debug configuration
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = (
            [
                path(
                    "media/<path:path>/",
                    django.views.static.serve,
                    {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
                ),
                path("__debug__/", include(debug_toolbar.urls)),
            ]
            + staticfiles_urlpatterns()
            + urlpatterns
    )
