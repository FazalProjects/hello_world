from django.contrib import admin

from .models import Member


class MemberAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name', 'created_on')

admin.site.register(Member, MemberAdmin)
