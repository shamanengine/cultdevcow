from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST


# Create your views here.

def index(request):
    return HttpResponse('ok')


# redirect
def my_view(request):
    # ...
    return redirect('/some/url')
