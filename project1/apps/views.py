from django.shortcuts import render,redirect
from apps.models import Student
from apps.forms import StudentForm

def home(request):
	stud=Student.objects.all()
	return render(request,'appfile/home.html', {'s':stud})

def forms(request):
	form=StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
		return final(request)
	return render(request,'appfile/form.html',{'form':form})

def final(request):
	return render(request,'appfile/final.html')

def delete(request,id):
	s=Student.objects.get(id=id)
	s.delete()
	return redirect('/home')

def update(request,id):
	student=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
		return redirect('/home')
	return render(request,'appfile/update.html',{'s':student})
