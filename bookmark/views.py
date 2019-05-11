from django.shortcuts import render

# Create your views here.

from .models import Bookmark

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy

class BookmarkList(ListView):
    model = Bookmark

class BookmarkDetail(DetailView):
    model = Bookmark

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_create'
    success_url = '/'

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_update'
    success_url = '/'
    #success_url = '/update/{pk}/'


class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = '/'


