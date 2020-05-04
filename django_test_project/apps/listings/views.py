from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend

from .models import Listing
from .serializers import ListingSerializer


class ListingViewSetBase(ListAPIView):

    serializer_class = ListingSerializer

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]
    filterset_fields = ["owner"]
    search_fields = ["label"]
    ordering_fields = [
        "published_at",
        "created_at",
    ]


class ListingViewSet(ListingViewSetBase):
    """
    List all the listings.

    This endpoint is accessible only by admin users as we don't want that regular user have access
    to draft or unpublished listings.
    """

    permission_classes = [IsAdminUser]
    queryset = Listing.objects.all()

    filterset_fields = ListingViewSetBase.filterset_fields + ["status"]


class ActiveListingViewSet(ListingViewSetBase):
    """
    List all the active listings.

    This endpoint is public and should be accessible by any user.
    """

    permission_classes = [AllowAny]
    queryset = Listing.objects.active()
