from django.db import models


class OtherThing(models.Model):
    pass


class Thing(models.Model):
    is_something = models.BooleanField()
    other_things = models.ManyToManyField(OtherThing)
