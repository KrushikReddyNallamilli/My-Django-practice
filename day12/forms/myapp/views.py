from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.forms import StudentForm
from myapp.models import Student
# Create your views here.

def register(request):
	if request.method=="POST":
		form=StudentForm(request.POST)
		form.save()
		return HttpResponse('Done')
	form=StudentForm()
	return render(request,'myapp/register.html',{'form':form})


def details(request):
	data=Student.objects.all()
	return render(request,'myapp/data.html',{'data':data})


def edit(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
		return redirect('/details')

	form=StudentForm(instance=data)

	return render(request,'myapp/edit.html',{'form':form,'data':data})