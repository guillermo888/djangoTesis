from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola mundio esta es mi primera aplicacion")