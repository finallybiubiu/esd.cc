from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from .models import Segmentfault
from .models import Segmentfault_Blog
from .models import V2EX

@cache_page(3600)
def index(req):
    return render_to_response('index.html')

@cache_page(3600)
def segmentfault_index(req):
    today = Segmentfault.objects.last().date
    result = {
            'count' : Segmentfault.objects.count(),
            'today' : today,
            'views' : Segmentfault.objects.filter(date=today).order_by('-view')[0:10],
            'marks' : Segmentfault.objects.filter(date=today).order_by('-mark')[0:10],
            'follows' : Segmentfault.objects.filter(date=today).order_by('-follow')[0:10],
            }
    return render_to_response('segmentfault_index.html',result)

@cache_page(3600)
def segmentfault_blog_index(req):
    today = Segmentfault_Blog.objects.last().date
    result = {
            'count' : Segmentfault_Blog.objects.count(),
            'today' : today,
            'views' : Segmentfault_Blog.objects.filter(date=today).order_by('-view')[0:10],
            'marks' : Segmentfault_Blog.objects.filter(date=today).order_by('-mark')[0:10],
            'recommend' : Segmentfault_Blog.objects.filter(date=today).order_by('-recommend')[0:10],
            }
    return render_to_response('segmentfault_blog_index.html',result)

@cache_page(3600)
def v2ex_index(req):
    today = V2EX.objects.last().idate
    data = V2EX.objects.filter(idate=today)
    result = {
            'count' : V2EX.objects.count(),
            'today' : today,
            'click' : data.order_by('-click')[0:10],
            'mark' : data.order_by('-mark')[0:10],
            'thank' : data.order_by('-thank')[0:10],
            #'comment' : data.order_by('-comment')[0:30],
            }
    return render_to_response('v2ex_index.html', result)

@cache_page(3600)
def v2ex_click(req):
    today = V2EX.objects.last().idate
    return render_to_response('v2ex_click.html', {
        'data' : V2EX.objects.filter(idate=today).order_by('-click')[0:200],
        })

@cache_page(3600)
def v2ex_mark(req):
    today = V2EX.objects.last().idate
    return render_to_response('v2ex_mark.html', {
        'data': V2EX.objects.filter(idate=today).order_by('-mark')[0:200],
        })

@cache_page(3600)
def v2ex_thank(req):
    today = V2EX.objects.last().idate
    return render_to_response('v2ex_thank.html', {
        'data': V2EX.objects.filter(idate=today).order_by('-thank')[0:200],
        })
