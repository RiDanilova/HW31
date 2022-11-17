from django.urls import path

from ads.views import AdListView, AdDetailView, AdUploadImageView, AdCreateView, AdUpdateView, AdDeleteView

urlpatterns = [
    path("", AdListView.as_view(), name="all_ads"),
    path("<int:pk>/", AdDetailView.as_view(), name="ad_detail"),
    path("create/", AdCreateView.as_view(), name="create_ad"),
    path("<int:pk>/upload_image/", AdUploadImageView.as_view(), name="ad_upload_image"),
    path("update/<int:pk>/", AdUpdateView.as_view(), name="update_ad"),
    path("delete/<int:pk>/", AdDeleteView.as_view(), name="delete_ad"),
]
