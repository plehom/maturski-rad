from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostsForm

# Create your views here.

class MainPage(ListView):
    model = Posts
    template_name = "index.html"

class CreatePost(LoginRequiredMixin,FormView):
    template_name = "create.html"
    form_class = PostsForm
    success_url = "/home"
    def form_valid(self, form):

        form.save()
        return super().form_valid(form)

