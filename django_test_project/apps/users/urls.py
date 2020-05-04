from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path(
        "owners/<int:pk>/",
        views.ListingOwnerView.as_view(),
        name="listings_owner_details",
    ),
    path("owners/", views.ListingOwnerViewSet.as_view(), name="listings_owners",),
]
