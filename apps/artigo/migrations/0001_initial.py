# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data_publicacao', models.DateField()),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo', models.TextField()),
                ('reporter', models.ForeignKey(to='reporter.Reporter')),
            ],
        ),
    ]
