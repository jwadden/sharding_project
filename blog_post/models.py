from django.db import models

from django_sharding_library.decorators import model_config
from django_sharding_library.fields import TableShardedIDField
from django_sharding_library.models import TableStrategyModel


class BlogPostModelIDs(TableStrategyModel):
    pass


@model_config(shard_group='shard_blog')
class BlogPost(models.Model):
    id = TableShardedIDField(primary_key=True, source_table=BlogPostModelIDs)
    title = models.CharField(max_length=120)
    author_pk = models.PositiveIntegerField()
    text = models.TextField(blank=True, default='')

    def get_shard(self):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=self.author_pk).shard
    
    @property
    def author(self):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=self.author_pk)
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.__unicode__()
