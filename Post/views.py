from django.shortcuts import render
from .models import Post, PostManger
from django.views.generic import ListView, DetailView


class Album(ListView):
    """This function return post list viwe which user can see all post in one or several page"""
    queryset = Post.objects.all()
    template_name = 'Album.html'
    paginate_by = 9


class Post_detail(DetailView):
    """ This function show each post in spesefied page """
    queryset = Post.objects.all()
    template_name = "post_detail.html"


    def get_context_data(self, *args, objects_list=None, **kwargs):
        context = super(Post_detail, self).get_context_data(*args, **kwargs)
        context['abc'] = "my name is Benyamin"
        print(context)
        return context


class search_in_post(ListView):
    template_name = 'Album.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        search_query = request.GET.get('q')

        if search_query is not None:
            return Post.objects.search(search_query)

        return Post.objects.none()
