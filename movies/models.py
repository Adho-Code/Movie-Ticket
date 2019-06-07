from django.db import models
from django.shortcuts import render,redirect
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime as dt
from django.shortcuts import get_object_or_404
# Create your models here.



class Movie(models.Model):
    movie_name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='movie',null=True)
    image_path = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.movie_name
    @classmethod
    def search_by_name(cls,search_term):
        movie = cls.objects.filter(movie_name__icontains = search_term)
        return movie


class Available(models.Model):
    name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)
    move = models.ForeignKey(Movie,blank=True, on_delete=models.CASCADE)
    path = models.ImageField(upload_to = 'gallery/')

    @classmethod
    def search_by_activity_name(cls,search_term):
        movies = Available.objects.filter(activity_name__icontains = search_term)
        return movies