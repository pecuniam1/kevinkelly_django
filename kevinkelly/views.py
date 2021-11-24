from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render

def json_response(request):
    return JsonResponse({"Message": "Hello World!"})

def html_template_response(request):
    return render(request, 'kevinkelly/hello_world.html')

# Create your views here.
