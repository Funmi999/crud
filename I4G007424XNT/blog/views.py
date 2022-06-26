from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from  django.shortcuts import render
import blog

from blog.models import Post

class postlistview(ListView):
    model = Post
    template = 'blog/post_list.html'
    

class postcreateview(CreateView):
    model = Post
    fields = "__all__"    
    success_url = reverse_lazy("blog:all")
    template ='blog/post_form.html'


class postdetailView(DetailView):
      model = Post
      template = 'blog/post_detail.html'

class  postupdateview(UpdateView):

       model = Post
       fields = "__all__"
       success_url = reverse_lazy("blog:all")
       template = 'blog/post_form.html'


class postdeleteview(DeleteView):     
   model = Post
   fields = "__all__"
   success_url  = reverse_lazy("blog:all")
   template = 'blog/post_confirm_delete.html'



