from django.contrib import admin
from django import forms

from .models import BlogPost

class BlogPostAdminForm(forms.ModelForm):
    author_pk = forms.ChoiceField()
    
    class Meta:
        model = BlogPost
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super(BlogPostAdminForm, self).__init__(*args, **kwargs)
        from django.contrib.auth import get_user_model
        
        self.fields['author_pk'].choices = [
            (author.pk, author.username) for author in get_user_model().objects.all()
        ]
        
        self.fields['author_pk'].label = 'Author'
        

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    
    def get_queryset(self, request):
        qs = BlogPost.objects.using('app_shard_001').all()
        
        return qs

admin.site.register(BlogPost, BlogPostAdmin)
