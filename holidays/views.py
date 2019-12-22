from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#def index(request):
	#return HttpResponse("Welcome in holidays")

def index(request):
	return render(request,'holidays/index.htm')	