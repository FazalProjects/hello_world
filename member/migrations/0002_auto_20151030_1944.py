# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('created_on',)},
        ),
        migrations.AlterField(
            model_name='member',
            name='created_on',
            field=models.DateTimeField(verbose_name='Created Date', auto_now_add=True),
        ),
    ]
