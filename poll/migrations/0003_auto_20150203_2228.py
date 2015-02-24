# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '0002_auto_20150203_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthByIpAndRemoteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=1024, verbose_name=b'Password or SSL_KEY')),
                ('authtype', models.CharField(max_length=100, choices=[(b'ssh', b'ssh-password'), (b'ssh-key', b'ssh-key')])),
                ('ip', models.ForeignKey(blank=True, to='poll.IP', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('group', models.ManyToManyField(to='poll.Group', null=True, blank=True)),
                ('ip', models.ManyToManyField(to='poll.IP', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RemoteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='polluser',
            name='remoteuser',
            field=models.ManyToManyField(to='poll.RemoteUser', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='polluser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authbyipandremoteuser',
            name='remoteUser',
            field=models.ForeignKey(blank=True, to='poll.RemoteUser', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='authbyipandremoteuser',
            unique_together=set([('ip', 'remoteUser')]),
        ),
    ]
