from django.shortcuts import render

# Create your views here.
def home(req):
	return render(req,'new/home.html')

def table(req):
	return render(req,'new/table1.html')