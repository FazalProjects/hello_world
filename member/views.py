import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .forms import MemberForm
from .models import Member

def member_add(request):
    form = MemberForm()
    data = {'form': form}
    return render(request, "member/add_member.html", data)

def member_save(request):
    form = MemberForm(request.POST)
    if form.is_valid():
        form.save()
        data = {'form': MemberForm(),
                'message': '%s - saved successfully'% form.cleaned_data['name']}
        return render(request, "member/add_member.html", data)
    else:
        data = {'form': form}
        return render(request, "member/add_member.html", data)

def member_api(request):
    #members = Member.objects.all()
    #data = serializers.serialize('json', members)
    members = Member.objects.values_list('name', flat=True)
    #data = json.dumps({'names' : members})
    data = serializers.serialize('json', members)
    return HttpResponse(data, content_type='application/json')