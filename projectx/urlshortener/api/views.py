from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from urlshortener.models import Short
from .serializers import ShortSerializer
from urlshortener.utils import random_hash



@api_view(['POST'])
def shortener(request):
	code = random_hash()
	context = Short(short_url=code)

	# to ensure that custom url is not passed
	if 'short_url' in request.data:
		del request.data['short_url']

	serializer = ShortSerializer(context, data=request.data)
	if serializer.is_valid():
		serializer.save()
		
		return Response({'short_url':request.build_absolute_uri('/') + code}, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def shortener_premium(request):
	serializer = ShortSerializer(data=request.data)
	
	if serializer.is_valid() and 'short_url' in request.data:  # to ensure that custom url is passed
		serializer.save()

		return Response({'short_url':request.build_absolute_uri('/') + request.data['short_url']}, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

