from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FromView, FormView
from .models import *


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'


class Post(DetailView):
    model = Post
    context_object_name = 'Post'


class PostCreate(CreateView):
    model = Post
    fields = '__all__'


# class Myform(FormView):
#     form_class = myform
#     success_url = '/success/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


