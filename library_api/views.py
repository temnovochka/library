from rest_framework import viewsets

from library_api import serializers
from library_api import models as library_models


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LanguageSerializer
    queryset = library_models.Language.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = library_models.Book.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Author
    queryset = library_models.Author.objects.all()


class FollowerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Follower
    queryset = library_models.Follower.objects.all()
