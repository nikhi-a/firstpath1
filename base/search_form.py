from django import forms
from .models import Company

class JobSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, label="Job Title")
    location = forms.CharField(max_length=100, required=False, label="Location")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'title' in self.data:
            self.fields['title'].initial = self.data['title']
        
        if 'location' in self.data:
            self.fields['location'].initial = self.data['location']

