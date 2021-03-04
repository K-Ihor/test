from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News_post, Comment
from django.db.models import F


class Home(ListView):
    model = News_post
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        context['comments'] = Comment.objects.all()
        return context


class Coment(ListView):
    model = Comment
    template_name = 'news/comment.html'
    context_object_name = 'comments'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Comments'
        return context


class GetComment(DetailView):
    model = Comment
    template_name = 'news/single.html'
    context_object_name = 'comment'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

