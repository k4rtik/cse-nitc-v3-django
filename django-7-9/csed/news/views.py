from django.shortcuts import render_to_response, get_object_or_404
from csed.news.models import NewsItem

def index(request):
    latest_news_items = NewsItem.objects.all().order_by('-pub_time')[:5]
    return render_to_response('news/index.html', {'latest_news_items': latest_news_items})

def archive(request):
    return HttpResponse("You are at the news archive")

def detail(request, newsitem_id):
    n = get_object_or_404(NewsItem, pk=newsitem_id)
    return render_to_response('news/detail.html', {'newsitem': n})
