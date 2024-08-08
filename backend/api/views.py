from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View

from .models import Author, Publisher
from .serializers import AuthorSerializer, PublisherSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class AuthorListView(View):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        serializer_author = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer_author.data, safe=False)

    def post(self):
        pass

@method_decorator(csrf_exempt, name='dispatch')
class PublisherListView(View):
    def get(self, request, *args, **kwargs):
        publishers = Publisher.objects.all()
        serializer_publisher = PublisherSerializer(publishers, many=True)
        return JsonResponse(serializer_publisher.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = request.POST
        ser = PublisherSerializer(data=data)
        if ser.is_valid():
            print(ser.validated_data)
            val = ser.save()
            return JsonResponse({'a':'helo'})

class PublisherDetailView(View):
    pass