# from ast import Return
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create yoyr view here
# @login_required(login_url="/accounts/login")
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html' ,{'articles' : articles})

@login_required(login_url="/accounts/login")
def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

# to auth page
@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

def article_test(request):
    return render(request, 'articles/article_test.html',)
