from django.core.management.base import BaseCommand, CommandError
from .models import *
import csv

class Command(BaseCommand):
    args = 'file_path'
    help = 'Imports from local csv file'


    def handle(self, file_name, *args, **options):
        file_name = file_name
        file_extension = '.csv'
        pwd = abspath(dirname(__file__))
        file_path = pwd + '/data/' + file_name + file_extension
        self.stdout.write(file_path, ending='')

        with open(file_path, 'rb'):
           rows = csv.reader(file, delimiter = ",", quotechar = '"')

           for row in rows:

              if rows.line_num == 1:
                 continue

              row[5] = row[5].replace("\n", " ")

              print "guid: " + row[0]
              print "user_id:  " + row[1]
              print "first_name:   " + row[2]
              print "last_name:   " + row[3]
              print "parent:  " + row[4]
              print "manager_guid: " + row[5]

              db_row = CornerstoneUserProfile(guid=row[0], user_id=row[1], first_name=row[2], last_name=row[3], parent= row[4], manager_guid=row[5])
              db_row.save()

           for user in CornerstoneUserProfile.objects.all():
              print user


