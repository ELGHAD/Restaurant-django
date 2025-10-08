# littlelemon/littlelemon/views.py
from django.http import HttpResponse

def dummy(request):
    return HttpResponse("OK")
