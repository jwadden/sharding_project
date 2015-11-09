from django.shortcuts import render

from django.views.generic import TemplateView

from blog_post.models import BlogPost

class HomePage(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        
        shards = ['app_shard_001', 'app_shard_002']
        
        blog_posts = {shard:BlogPost.objects.using(shard).all() for shard in shards}
                
        context['blog_posts'] = blog_posts
        
        return context
