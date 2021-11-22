from rest_framework.viewsets import ModelViewSet
from scrumboard.serializers import ListSerializer,CardSerializer
from scrumboard.models import List,Card

"""
    ModelViewSet allows GET PUT POST DELETE
"""
from scrumboard.serializers import CardSerializer, ListSerializer


class ListViewSet(ModelViewSet):
    queryset = List.objects.all() #aici practic colecatam toate obiectele din DB
    serializer_class = ListSerializer #django rest framework

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer