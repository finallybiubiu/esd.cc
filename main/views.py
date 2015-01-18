from django.shortcuts import render_to_response
from .models import Segmentfault

def index(req):
    return render_to_response('index.html') 

def segmentfault_index(req):
    result = {
            'count' : Segmentfault.objects.count(),
            'views' : Segmentfault.objects.order_by('-view')[0:10],
            'marks' : Segmentfault.objects.order_by('-mark')[0:10],
            'follows' : Segmentfault.objects.order_by('-follow')[0:10],
            }
    return render_to_response('segmentfault_index.html',result)
