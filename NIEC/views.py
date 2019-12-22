

from django.shortcuts import render
from  django.http import HttpResponse
#from . models import Mymodel2 
# Create your views here.

#def index(request):
	#return HttpResponse("Welcome to Events")

def index(request):
	return render(request,'NIEC/index.htm')
'''def index(request):
	context = {}
	context['data'] = Mymodel2.objects.all()
	return render(request, 'events/index.htm',context)
'''