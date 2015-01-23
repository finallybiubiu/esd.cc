from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from .models import Segmentfault
from .models import Segmentfault_Blog

@cache_page(30*60)
def index(req):
    return render_to_response('index.html')

@cache_page(30*60)
def segmentfault_index(req):
    today = Segmentfault.objects.last().date
    result = {
            'count' : Segmentfault.objects.count(),
            'views' : Segmentfault.objects.filter(date=today).order_by('-view')[0:10],
            'marks' : Segmentfault.objects.filter(date=today).order_by('-mark')[0:10],
            'follows' : Segmentfault.objects.filter(date=today).order_by('-follow')[0:10],
            }
    return render_to_response('segmentfault_index.html',result)

@cache_page(30*60)
def segmentfault_blog_index(req):
    today = Segmentfault_Blog.objects.last().date
    result = {
            'count' : Segmentfault_Blog.objects.count(),
            'views' : Segmentfault_Blog.objects.filter(date=today).order_by('-view')[0:10],
            'marks' : Segmentfault_Blog.objects.filter(date=today).order_by('-mark')[0:10],
            'recommend' : Segmentfault_Blog.objects.filter(date=today).order_by('-recommend')[0:10],
            }
    return render_to_response('segmentfault_blog_index.html',result)
