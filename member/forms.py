from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=30)
    class Meta:
        model = Member
        fields = ['name']