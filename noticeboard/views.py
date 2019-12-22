from django.shortcuts import render
from  django.http import HttpResponse
from . models import Update
# Create your views here.

#def index(request):
	#return HttpResponse("Welcome to Events")

#def index(request):
	#return render(request,'events/index.htm')
def index(request):
	context = {}
	context['data'] = Update.objects.all()
	return render(request, 'noticeboard/index.htm',context)
