from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<center><h1>welcome to Apssdc Django Class</h1></center>")