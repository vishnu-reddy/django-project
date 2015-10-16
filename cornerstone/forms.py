import csv
import StringIO
from django import forms
from .models import CornerstoneUserProfile


class CornerstoneUserProfileForm(forms.ModelForm):

    class Meta:

        model = CornerstoneUserProfile
        fields = ['user_id', 'first_name', 'last_name']

        def user_id_clean(self):
            user_id = self.cleaned_data.get('user_id', '')
            if CornerstoneUserProfile.objects.filter(user_id = user_id).count() > 0:
                raise forms.ValidationError(" Already in DB")
