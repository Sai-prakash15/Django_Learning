from django.db import models


# Create your Models here.

#model inheritance of timestamp parent class

class Timestamp(models.Model):
    modifieddate = models.DateField(auto_now=True)
    createddate = models.DateField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.modifieddate

    class Meta:
        verbose_name = "Timestamp"
        verbose_name_plural = "Timestamps"


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

class Reporter(Timestamp):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Articler(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


# one to one


class Place(Timestamp):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

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

    def __str__(self):  # __unicode__ on Python 2
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

    def __str__(self):  # __unicode__ on Python 2
        return self.content_title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"


# Vehicle , car , truck => where car and truck inherit from

class Vehicle(models.Model):
    lp_number = models.CharField(max_length=20, unique=True)
    wheel_count = models.IntegerField()
    manufacturer =  models.CharField(max_length=100)
    model_name  = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.lp_number

class Car(Vehicle):
    is_air_conditioned = models.BooleanField( blank=False)
    has_roof_top = models.BooleanField( blank=False)
    trunk_space =  models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return self.lp_number

class Truck(Vehicle):
    is_semi_truck = models.BooleanField( blank=False)
    max_goods_weight = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return self.lp_number

