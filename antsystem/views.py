from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola mundo esta es mi aplicacion de django")