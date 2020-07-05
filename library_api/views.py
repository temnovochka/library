from django.db import models
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, filters
from rest_framework.exceptions import ValidationError

from library_api import models as library_models
from library_api import serializers
from library_api.mail import notify_all_new_book


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LanguageSerializer
    queryset = library_models.Language.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = library_models.Book.objects.all()

    def perform_create(self, serializer):
        book = serializer.save()
        notify_all_new_book(book)


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Author
    queryset = library_models.Author.objects.all()


class FollowerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Follower
    queryset = library_models.Follower.objects.all()


class BookSearchFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        author_number = request.query_params.get('author_number', None)
        if author_number is None:
            raise ValidationError(detail='parameter "author_number" is required')
        return queryset.annotate(
            author_number=models.Count('authors')
        ).filter(author_number=author_number)


class BookSearchList(generics.ListAPIView):
    queryset = library_models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = [BookSearchFilterBackend]
    filterset_fields = ['author_number']

    @method_decorator(swagger_auto_schema(manual_parameters=[
        openapi.Parameter(name='author_number', in_=openapi.IN_QUERY, type='integer', description='Количество авторов',
                          required=True)],
    ), name='search')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
