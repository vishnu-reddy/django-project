from django import forms

from .models import CornerstoneUserProfile

class CornerstoneUserProfileForm(forms.ModelForm):

    class Meta:

        model = CornerstoneUserProfile
        fields = '__all__'
