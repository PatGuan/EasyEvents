# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150102_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
                ('group_members', models.CharField(max_length=20)),
                ('host', models.ForeignKey(to='events.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
