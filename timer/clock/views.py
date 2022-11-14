from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time, datetime
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def clock(request):
    return render(request, 'clock.html')

def hello(request):
    return render(request, 'hello.html')

def pomo(request):
    return render(request, 'pomo.html')

def stopwatch(request):
    return render(request, 'stopwatch.html')

def ajax(request):
    return render(request, 'ajax.html')

def test1(request):
    today = datetime.today().second
    context = {"date":today}
    return render(request, "test1.html", context = context)

def index(request):
    return render(request, "index.html")

@csrf_exempt
def send(request):
    # POST 요청일 때
    if request.method == 'POST':
        print(time.strftime('%S', time.localtime(time.time())))
        now = time.strftime('%S', time.localtime(time.time()))
        data = json.loads(request.body)
        # do something
        print(data['study'])
        if now == "05" or now == "06":
            context = {'study':False}
        else:
            context = {'study':True}
        
        return JsonResponse(context)

def check(request):
    if request.is_ajax():
        #do something
        request_data = request.POST
        return HttpResponse("OK")