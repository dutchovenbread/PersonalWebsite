from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request):
    return HttpResponse("<!DOCTYPE html><html><title>Michael Hunter's Homepage</title><body><h1>Michael Hunter</h1></body></html>")

