# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_sharding_library.fields
import django_sharding_library.id_generation_strategies
import blog_post.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', django_sharding_library.fields.TableShardedIDField(source_table=blog_post.models.BlogPostModelIDs, serialize=False, primary_key=True, strategy=django_sharding_library.id_generation_strategies.TableStrategy(backing_model=blog_post.models.BlogPostModelIDs))),
                ('title', models.CharField(max_length=120)),
                ('author_pk', models.PositiveIntegerField()),
                ('text', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostModelIDs',
            fields=[
                ('id', django_sharding_library.fields.BigAutoField(serialize=False, primary_key=True)),
                ('stub', models.NullBooleanField(default=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
