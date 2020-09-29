from django.db import models

# Create your models here.
class Student(models.Model):
	branches=[('CSE','cse'),
	          ('ECE','ece'),
	          ('MECH','mech'),
	          ('IT','it')]


	stuid=models.CharField(max_length=10)
	stuName=models.CharField(max_length=50)
	branch=models.CharField(max_length=50,choices=branches)
	age=models.IntegerField()


	def _str_(self):
		return self.stuid+" "+self.stuName