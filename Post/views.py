from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView



class Album(ListView):
    """This function return post list viwe which user can see all post in one or several page"""
    queryset = Post.objects.all()
    template_name = 'Album.html'


class Post_detail(DetailView):
    """ This function show each post in spesefied page """
    queryset = Post.objects.all()
    template_name = "post_detail.html"

    def get_context_data(self, *args, objects_list=None, **kwargs):
        context = super(Post_detail, self).get_context_data(
            *args, **kwargs)
        return context
