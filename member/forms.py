from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    """
    Model form for member
    """
    name = forms.CharField(label='Name', max_length=30)

    class Meta:
        model = Member
        fields = ['name']
