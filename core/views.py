from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST


# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def redirect_index(request):
    return redirect('/index')


@require_GET
def logo(request):
    return render(request, 'core/logo.html')


@require_GET
def moonspeak(request):
    return render(request, 'core/moonspeak.html')


# redirect
def my_view(request):
    # ...
    return redirect('/some/url')


@require_GET
def topic_details(request, pk):
    return render(request, 'core/topic_details.html')