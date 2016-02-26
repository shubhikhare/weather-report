from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from weather_api.models import City
from .forms import CityForm
import urllib2
import json
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
		return render(request, "register.html")

def login(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			username=request.POST['username']
			password=request.POST['password']
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					print "loggedin"
					auth.login(request,user)
					return HttpResponseRedirect("/weather")
			else:
				print "none"
				return HttpResponseRedirect("/register")

		elif request.method == "GET":
			return render(request,"login.html")

def weather(request):
	form=CityForm()
	if request.method=='POST':
		form=CityForm(request.POST)
		if form.is_valid():
			form.save()
		try:
			city=list(City.objects.values())
			response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + str(city[-1]['city']) + '&appid=2492488650dceb2ac012c8faa23dffc6')
			data = json.load(response)
			temp = str(data['main']['temp']-273)+ "C"

		except City.DoesNotExist:
			pass
		return render(request, "weather_result.html", {'city': form, 'temp': temp})
	elif request.method=="GET":
		return render(request, "weather.html")
		
def logout(request):
	return render(request, "index.html")