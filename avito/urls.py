from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads.views import root
from avito import settings
from rest_framework import routers

from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register("location", LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", root),

    path("cat/", include("ads.urls.category_urls")),
    path("ad/", include("ads.urls.ad_urls")),
    path("user/", include("users.urls")),
    path("selection/", include("ads.urls.selection_urls")),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
