from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime

def index(request):
        return HttpResponse('<html><body>Hello Hello</body></html>')

def something(request):
        return HttpResponse('<html><body>Something. Ta da!</body></html>')

def anything(request):
        t = loader.get_template('anything.html')
        c = Context({'current_time': datetime.now(), })
        return HttpResponse(t.render(c))


# Create your views here.
