from django.db import models

# Create your models here.

class Tag(models.Model):
    name         = models.CharField(max_length=256, blank=True, null=True, default = None, db_index = True)
    
    top_tracks   = models.ManyToManyField('main.Track', through='main.TagTopTrack')

class TagTopTrack(models.Model):
    tag          = models.ForeignKey('main.Tag', null=True, default = None)
    track        = models.ForeignKey('main.Track', null=True, default = None)
    
    rank         = models.IntegerField(blank=True, null=True, default = None, db_index = True)

class Track(models.Model):
    title        = models.CharField(max_length=256, blank=True, null=True, default = None, db_index = True)
    artist       = models.ForeignKey('main.Artist', null=True, default = None)

    top_tags     = models.ManyToManyField('main.Tag', through='main.TrackTopTag')
    similar      = models.ManyToManyField('main.Track', through='main.TrackSimilar')

class TrackTopTag(models.Model):
    track        = models.ForeignKey('main.Track', null=True, default = None)
    tag          = models.ForeignKey('main.Tag', null=True, default = None)

    weight       = models.IntegerField(blank=True, null=True, default = None, db_index = True)

class TrackSimilar(models.Model):
    tfrom        = models.ForeignKey('main.Track', related_name='similar_to', null=True, default = None)
    tto          = models.ForeignKey('main.Track', related_name='similar_from', null=True, default = None)

    match        = models.FloatField(blank=True, null=True, default = None, db_index = True)

class Artist(models.Model):
    name         = models.CharField(max_length=256, blank=True, null=True, default = None, db_index = True)
    