from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Stores
from .serializers import StoreSerializer


class StoreViewAPI(ListAPIView):

    queryset = Stores.objects.all()
    serializer_class = StoreSerializer


class StoreRetrieveAPI(RetrieveAPIView):

    queryset = Stores.objects.all()
    serializer_class = StoreSerializer


class StoreViewSet(ModelViewSet):
    """
        retrieve:
            Return the given store.

        list:
            Return a list of all stores.

        create:
            Create a new store.

        destroy:
            Delete a store.

        update:
            Update a store.

        partial_update:
            Update a store.
    """

    queryset = Stores.objects.all()
    serializer_class = StoreSerializer