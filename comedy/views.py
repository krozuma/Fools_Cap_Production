from django.shortcuts import render
from django.http import Http404
from .filters import ArtFilter
from .models import Article

def index(request):
    a_list = Article.objects.all().order_by('rank', '-pub_date')
    context = {'article_list': a_list}
    return render(request, 'comedy/index.html', context)

def detail(request, slug, art_id):
    try:
        art = Article.objects.get(pk=art_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist') 
    return render(request, 'comedy/detail.html', context={'art': art})

def news(request):
    art = Article.objects.filter(art_cat='NE').order_by('rank', '-pub_date')
    context={'art': art}
    return render(request, 'comedy/news.html', context)

def politics(request):
    art = Article.objects.filter(art_cat='PO').order_by('rank', '-pub_date')
    context={'art': art}
    return render(request, 'comedy/politics.html', context)

def local(request):
    art = Article.objects.filter(art_cat='LO').order_by('rank', '-pub_date')
    context={'art': art}
    return render(request, 'comedy/local.html', context)

def sports(request):
    art = Article.objects.filter(art_cat='SP').order_by('rank', '-pub_date')
    context={'art': art}
    return render(request, 'comedy/sports.html', context)

def entertainment(request):
    art = Article.objects.filter(art_cat='EN').order_by('rank', '-pub_date')
    context={'art': art}
    return render(request, 'comedy/entertainment.html', context)

def opinion(request):
    art = Article.objects.filter(art_cat='OP').order_by('rank', '-pub_date')
    context={'art': art}
    return render(request, 'comedy/opinion.html', context)

def health(request):
    art = Article.objects.filter(art_cat='HE').order_by('rank', '-pub_date')
    context={'art': art}
    return render(request, 'comedy/health.html', context)
