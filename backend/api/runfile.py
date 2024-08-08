from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import AuthorSerializer, PublisherSerializer
from .models import Author, Publisher

ax = Author.objects.last()

ser_ax = AuthorSerializer(ax)
print(ser_ax.data)