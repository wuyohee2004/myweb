# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20150203_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpsLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(null=True, blank=True)),
                ('log_type', models.CharField(max_length=50)),
                ('poll_user', models.CharField(max_length=30)),
                ('run_user', models.CharField(max_length=30)),
                ('cmd', models.TextField()),
                ('total_task', models.IntegerField()),
                ('success_num', models.IntegerField()),
                ('failed_num', models.IntegerField()),
                ('track_mark', models.IntegerField(unique=True)),
                ('note', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpsLogTemp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=30)),
                ('ip', models.IPAddressField()),
                ('event_type', models.CharField(max_length=50)),
                ('cmd', models.TextField()),
                ('event_log', models.TextField()),
                ('result', models.CharField(default=b'unknown', max_length=30)),
                ('track_mark', models.IntegerField(blank=True)),
                ('note', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
