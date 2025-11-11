from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item, Country
from .serializers import ItemSerializer, CountrySerializer

@api_view(['GET'])
def getData(request):
	items = Item.objects.all()
	serializer = ItemSerializer(items, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def getCountries(request):
	countries = Country.objects.all()
	serializer = CountrySerializer(countries, many=True)
	return Response(serializer.data)