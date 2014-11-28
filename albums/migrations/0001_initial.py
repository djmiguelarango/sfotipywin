# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=140)),
                ('cover', models.ImageField(upload_to='album')),
                ('artist', models.ForeignKey(to='artists.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]