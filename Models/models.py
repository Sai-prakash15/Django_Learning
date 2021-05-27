from django.db import models
from django.core.exceptions import ValidationError

# presave so clean would be invoked before save automatically
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
# from django.contrib.sessions import Session

# @receiver(pre_save)
# def pre_save_handler(sender, instance, *args, **kwargs):
#     if not isinstance(instance, Session):
#         instance.full_clean()
#     instance.full_clean()


# Create your Models here.

# model inheritance of timestamp parent class (Abstract inheritance)

class Timestamp(models.Model):
    modifieddate = models.DateField(auto_now=True)
    createddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.modifieddate)

    class Meta:
        verbose_name = "Timestamp"
        verbose_name_plural = "Timestamps"
        abstract = True


# Relationships and meta options
# many-many
class Publication(Timestamp):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']


# many to one

class Reporter(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


class Articler(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


# one to one
class PlaceX(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, blank=True)

    class Meta:
        indexes = [models.Index(fields=['name', ]), ]

    def __str__(self):
        return "%s the place" % self.name

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, blank=True)

    class Meta:
        indexes = [models.Index(fields=['name', ]), ]

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


## Model inheritance (BTS one to one relationship)

import uuid


class Content(models.Model):
    content_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content_slug = models.CharField(max_length=100, unique=True)
    content_title = models.CharField(max_length=100)
    content_subtitle = models.CharField(max_length=255, null=True, blank=True)
    content_headline = models.CharField(max_length=100)

    def __str__(self):
        return self.content_title

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Content"


class Video(Content):
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_link = models.URLField(null=True, blank=True)
    video_source_guid = models.CharField(max_length=255, null=True, blank=True)
    video_embed = models.TextField(null=True, blank=True)
    video_copyright = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.content_title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"


# Vehicle , car , truck => where car and truck inherit from
# Multi-table inheritance
class Vehicle(models.Model):
    lp_number = models.CharField(max_length=20, unique=True)
    wheel_count = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100, null=True, blank=True)

    def clean(self):
        if self.wheel_count <= 1 and self.wheel_count is not None:
            raise ValidationError(('Wheel count must be greater than 1'), code='invalid')

    def __str__(self):
        return self.lp_number


class Car(Vehicle):
    is_air_conditioned = models.BooleanField(blank=False)
    has_roof_top = models.BooleanField(blank=False)
    trunk_space = models.FloatField()

    def __str__(self):
        return self.lp_number


class Truck(Vehicle):
    is_semi_truck = models.BooleanField(blank=False)
    max_goods_weight = models.FloatField()

    def __str__(self):
        return self.lp_number


class InformationX(models.Model):
    content = models.CharField(max_length=20)

    def __str__(self):
        return self.content


class TaskX(models.Model):
    taskName = models.CharField(max_length=20)

    def __str__(self):
        return self.taskName

# Model X
class Person(models.Model):
    name = models.CharField(max_length=50)
    task = models.ForeignKey(TaskX, on_delete=models.CASCADE); #many humans can work on one particular task
    place = models.OneToOneField(PlaceX, on_delete=models.CASCADE);
    information = models.ManyToManyField(InformationX)

    def __str__(self):
        return self.name



class VehicleXx(models.Model):
    person =  models.ForeignKey(Person, on_delete=models.CASCADE); #  One herson can own many vehicles
    lp_number = models.CharField(max_length=20, unique=True)
    wheel_count = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100, null=True, blank=True)

    def clean(self):
        if self.wheel_count <= 1 and self.wheel_count is not None:
            raise ValidationError(('Wheel count must be greater than 1'), code='invalid')

    def __str__(self):
        return self.lp_number



#Model for scenario 10

class Temp(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name