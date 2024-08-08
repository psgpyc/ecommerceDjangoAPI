from rest_framework import serializers

from api.models import Author, Publisher


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)

    def create(self, validated_data):
        instance = Publisher.objects.create(**validated_data)
        return instance

    def save(self, **kwargs):
        print(self)
        print(self.validated_data)
        super().save(**kwargs)
