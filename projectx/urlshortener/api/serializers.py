from rest_framework.serializers import ModelSerializer

from urlshortener.models import Short


class ShortSerializer(ModelSerializer):
	class Meta:
		model = Short
		fields = ['full_url', 'short_url']