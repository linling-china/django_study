from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogArticles
# Create your views here.
from django.http import HttpRequest, HttpResponse

@login_required()
def blog_titles(request):
    if request.user.is_authenticated:
#        return HttpResponse(request.user.)
        blogs = BlogArticles.objects.all()
        return render(request, 'blog/titles.html', {'blogs':blogs})
    else :
        return HttpResponse('ERROR - login please!')

@login_required()
def blog_arctile(request, article_id):
#    article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, 'blog/content.html', {'article':article, "publish":pub})