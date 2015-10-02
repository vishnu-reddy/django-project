from django.shortcuts import render
from models import CornerstoneUserProfile

# Creating views

def cornerstone_profiles_list(request):

     manager_names = []
     nodes = CornerstoneUserProfile.objects.all()
     count = CornerstoneUserProfile.objects.count()
     for id in range(0, count):
         users = CornerstoneUserProfile.objects.filter(user_id = id)
         if users:
             managers = CornerstoneUserProfile.objects.filter(parent_id = id)
             for manager in managers:
                 if not manager.user_id in manager_names:
                     print manager.user_id
                     for user_data in users:
                         print user_data

                     manager_names.append(manager.user_id)

     return render(request, 'base.html', {'nodes' : nodes})





