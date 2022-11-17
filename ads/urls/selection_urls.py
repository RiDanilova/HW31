from django.urls import path

from ads.views import SelectionListView, SelectionDetailView, SelectionCreateView, SelectionUpdateView, \
    SelectionDeleteView

urlpatterns = [
    path("", SelectionListView.as_view(), name="all_selections"),
    path("<int:pk>/", SelectionDetailView.as_view(), name="selection_detail"),
    path("create/", SelectionCreateView.as_view(), name="create_selection"),
    path("update/<int:pk>/", SelectionUpdateView.as_view(), name="update_selection"),
    path("delete/<int:pk>/", SelectionDeleteView.as_view(), name="delete_selection"),
]