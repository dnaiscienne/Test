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

#lol this should get replaced...
def identify_examinee(request):
        t = loader.get_template('testApp/identify_examinee.html')
        c = Context({'current_time': datetime.now(), })
        return HttpResponse(t.render(c))

#look another lame stub method thingy. Tovarisch help me...
def load_test(request, online_test_id):
	t = loader.get_template('testApp/online_test.html')
        c = Context({'current_time': datetime.now(), })
        return HttpResponse(t.render(c))
	


# Create your views here.
