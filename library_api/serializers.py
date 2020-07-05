from rest_framework import serializers

from library_api import models as library_models


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = library_models.Language
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(queryset=library_models.Language.objects.all(), many=True)
    authors = serializers.PrimaryKeyRelatedField(queryset=library_models.Author.objects.all(), many=True,
                                                 required=False)

    class Meta:
        model = library_models.Book
        fields = ['id', 'name', 'year', 'languages', 'authors']


class Author(serializers.ModelSerializer):
    class Meta:
        model = library_models.Author
        fields = '__all__'


class Follower(serializers.ModelSerializer):
    class Meta:
        model = library_models.Follower
        fields = '__all__'
