from django.shortcuts import render
from .models import CornerstoneUserProfile
from .forms import CornerstoneUserProfileForm

def cornerstone_profiles_list(request):
    if request.method == 'POST':
      form = CornerstoneUserProfileForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request, "base.html", {'form': form})
    else:
       form = CornerstoneUserProfileForm()

    nodes = CornerstoneUserProfile.objects.all()
    return render(request, "base.html", {'form': form, 'nodes': nodes})