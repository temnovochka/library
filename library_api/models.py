from django.db import models


class Language(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, primary_key=True)


class Book(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    languages = models.ManyToManyField(Language, related_name='books', related_query_name='book')
    year = models.IntegerField(verbose_name='Год публикации')
    authors = models.ManyToManyField('Author', related_name='books', related_query_name='book', blank=True)


class Person(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255)


class Author(Person):
    pass


class Follower(Person):
    email = models.EmailField(verbose_name='Электронный адрес')
