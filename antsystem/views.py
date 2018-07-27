from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("Hola esta es un aprueba del httpresponse")
#return render(request,'index.html',context={'num_books':"num_books",'num_instances':"num_instances",'num_instances_available':"num_instances_available",'num_authors':"num_authors"},)