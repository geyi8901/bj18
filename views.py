from django.htpp import HttpResponse

def index(request):
    return HttpResponse('OK')
