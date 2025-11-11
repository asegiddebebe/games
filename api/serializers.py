from rest_framework import serializers
from base.models import Item, Country

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item,
		fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = "__all__"