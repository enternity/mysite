from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.template import RequestContext
from .models import Article


def get_redirected(queryset_or_class, lookups, validators):
    '''
        Call get_object_or_404 and conditionally build redirect URL
    '''
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj,key):
            return obj.get_absolute_url()
    return None

class ArticleView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleListView(ListView):
    model = Article
    pass

def article_detail(request, id, slug):
    article_url = get_redirected(Article, {'pk': id}, {'slug': slug})
    if article_url:
        return redirect(article_url)
    
    else:
        #404 error
        pass