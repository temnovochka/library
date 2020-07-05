from django.db import models


class Language(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)


class Book(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    language = models.ManyToManyField(Language, related_name='books', related_query_name='book')
    year = models.IntegerField(verbose_name='Год публикации')
    author = models.ManyToManyField('Author', related_name='books', related_query_name='book')


class Person(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255)


class Author(Person):
    pass


class Follower(Person):
    email = models.EmailField(verbose_name='Электронный адрес')
