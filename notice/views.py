

from django.shortcuts import render
from  django.http import HttpResponse
from django.urls import path,include
from . models import Mynotice
# Create your views here.

#def index(request):
	#return HttpResponse("Welcome to Events")

#def index(request):
	#return render(request,'events/index.htm')
def index(request):
		context = {}
		context['data'] = Mynotice.objects.all()
		return render(request, 'notice/index.htm',context)

def click(request):
	
	return path('events/',include('events.urls')),
	#return render(request,'events/index.com')