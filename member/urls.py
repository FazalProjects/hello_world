from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    url(r'^$', views.member_add),
    url(r'^add/$', views.member_add, name='member_add'),
    url(r'^save/$', views.member_save, name='member_save'),
    url(r'^api/$', views.member_api, name='member_api'),
    url(r'^api-token-auth/', obtain_auth_token),
]
