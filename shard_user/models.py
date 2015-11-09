from django.contrib.auth.models import AbstractUser

from django_sharding_library.models import ShardedByMixin

class User(AbstractUser, ShardedByMixin):
    django_sharding__shard_group = 'shard_blog'
