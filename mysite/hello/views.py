from django.http import HttpResponse

def owner(request):
    return HttpResponse("Hello, world. 28869ca3 is the polls index.")
# Create your views here.


def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '28869ca3', max_age=1000)
    return resp
