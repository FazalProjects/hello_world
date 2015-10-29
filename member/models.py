from django.db import models

class Member(models.Model):
    name = models.CharField("Member Name", max_length=30)
    created_on = models.DateTimeField("Created Date", auto_now_add=True)
    def __str__(self):
        return self.name
