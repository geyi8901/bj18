from django.htpp import HttpResponse
from django.shortcuts import redirect
def index(request):
    return HttpResponse('OK')
