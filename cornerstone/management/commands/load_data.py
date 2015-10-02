from django.core.management.base import BaseCommand
from cornerstone.models import *
import csv

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

class Command(BaseCommand):
    args = BASE_DIR  + "/data/CSOD_Users.csv"
    help = 'Imports from local csv file'
    def handle(self, *args, **options):
        if args:
            file_path = args[0]
        else:
            raise CommandError('provide a path for csv')

        with open(file_path) as file:
            rows = csv.reader(file, delimiter = ",", quotechar = '"')
            for row in rows:
                if set(row).pop() == "":
                    pass
                else:
                    for data in row:
                        print data

                        if rows.line_num == 1:
                            continue
                        print "guid:  " + row[0]
                        print "user_id:  " + row[1]
                        print "first_name:   " + row[2]
                        print "last_name:   " + row[3]

                        CornerstoneUserProfile.objects.update_or_create(guid = row[0], user_id = row[1], first_name = row[2], last_name = row[3])

            # adding parent
            file.seek(0)
            for row in rows:
                try:
                    user = CornerstoneUserProfile.objects.get(user_id = row[1])
                    parent = CornerstoneUserProfile.objects.get(user_id = row[4])
                    user.parent = parent
                    user.save()
                except:
                    pass










