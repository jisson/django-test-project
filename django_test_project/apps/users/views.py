from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import ListingOwner
from .serializers import ListingOwnerSerializer


class ListingOwnerView(RetrieveAPIView):
    queryset = ListingOwner.objects.all()
    serializer_class = ListingOwnerSerializer


class ListingOwnerViewSet(ListAPIView):
    queryset = ListingOwner.objects.all()
    serializer_class = ListingOwnerSerializer
