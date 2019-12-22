from django.shortcuts import render
from  django.http import HttpResponse
from . models import Question
# Create your views here.

def index(request):
	context = {}
	context['data'] = Question.objects.all()
	return render(request, 'app/index.htm',context)

