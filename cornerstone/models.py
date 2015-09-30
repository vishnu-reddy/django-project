import csv
from os.path import abspath,dirname
from django.db import models, transaction

from mptt.models import TreeForeignKey, MPTTModel #third party import

# model for creating cornerstoneuserprofile


class CornerstoneUserProfile(MPTTModel):

    guid = models.UUIDField(unique=True)
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True )  # parent is nothing but manager_id
    manager_guid = models.UUIDField(unique=True)

    def __str__(self):
        return "(%s), %s, %s)" % (self.parent, self.first_name,self.last_name)


