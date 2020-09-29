from django.shortcuts import render
from django.http import HttpResponse
import random
import qrcode

# Create your views here.
otp=0
def login(request):
	return render(request,'fapp/login.html')

def validate_user(request):
	if request.method=="POST":
		uname=request.POST['uname']
		upassword=request.POST['upassword']
		if uname=="Krushik" and upassword=="apssdc@123":
			rno=random.randint(1000,9999)
			global otp
			otp=rno
			im=qrcode.make("Your otp is :"+str(otp))
			im.save('fapp/static/qrimages/pic1.jpg')
			return render(request,'fapp/qrcode.html')
		else:
			return httpResponse ("wrong credentials")

def validate_otp(request):
	if request.method=="POST":
		uotp=request.POST['uotp']
		if otp==int(uotp):
			return render(request,'fapp/welcome.html')
		else:
			return httpResponse("Invalid Otp")
