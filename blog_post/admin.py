from django.contrib import admin

from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = BlogPost.objects.using('app_shard_001').all()
		
		return qs

admin.site.register(BlogPost, BlogPostAdmin)
