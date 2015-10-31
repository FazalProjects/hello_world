from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
from .forms import MemberForm
from .models import Member
from .serializers import MemberListSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def member_add(request):
    """
    Add Member Screen
    """
    form = MemberForm()
    data = {'form': form}
    return render(request, "member/add_member.html", data)


def member_save(request):
    """
    Save Member method
    """
    form = MemberForm(request.POST)
    if form.is_valid():
        form.save()
        data = {'form': MemberForm(),
                'message': '%s - saved successfully' % form.cleaned_data['name']}
        return render(request, "member/add_member.html", data)
    else:
        data = {'form': form}
        return render(request, "member/add_member.html", data)


def member_api(request):
    """
    Get all member name REST API
    """
    members = Member.objects.all()
    serializer = MemberListSerializer(members)
    return JSONResponse(serializer.data)


# Test
# def member_api(request):
#     members = Member.objects.values_list('name', flat=True)
#     data = json.dumps({'names' : list(members)})
#     return HttpResponse(data, content_type='application/json')
#
