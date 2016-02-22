from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
# Create your views here.

def  home(request):
	return render(request, 'index.html')

def signup(request):
	'''Signup for user'''
	if request.method == 'POST':
		print "Entered the if Section"
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		try:
			print "Entered the try section"
			user=User.objects.create_user(username=username,email=email,password=password)
			user.save()
			return HttpResponseRedirect("/login")
		except:
			return render(request,"register.html")

	elif request.method=='GET':
		return render(request,"register.html")

	else:
		return HttpResponseRedirect("/")

def login(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			username=request.POST['username']
			password=request.POST['password']
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					return HttpResponseRedirect("/weather")
			else:
				return render(request,"login.html",{"error":1})

		elif request.method == "GET":
			return render(request,"login.html")
	else:
		return HttpResponseRedirect("/login")

def  weather(request):
	return render(request, "weather.html")

def logout(request):
	return render(request, "index.html")

def weather_update(request):
	return render(request, "weather.html")