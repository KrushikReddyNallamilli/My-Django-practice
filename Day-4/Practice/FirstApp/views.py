from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
	return HttpResponse("<center><h1>This is my Django Project</h1></center>")


def hello(req):
	name="Krushik"
	return HttpResponse('hello viewer ,welcome to my page '+name)

def hi(req,name):
	return HttpResponse("hii "+name)

def rollno(req,rollno):
	return HttpResponse('My rollno is {}: '.format(rollno))

def task(req,nm,rno):
	return HttpResponse('My name is {} and My rollno is {} '.format(nm,rno))