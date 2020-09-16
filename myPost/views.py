from django.shortcuts import render
from .models import my_post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class my_post_list_view(ListView):
    queryset = my_post.objects.all()
    template_name = "card_list.html"


class my_post_detail_view(DetailView):
    queryset = my_post.objects.all()
    template_name = "post_detail.html"

    def get_context_data(self, *args, objects_list=None, **kwargs):
        context = super(my_post_detail_view, self).get_context_data(*args, **kwargs)
        return context