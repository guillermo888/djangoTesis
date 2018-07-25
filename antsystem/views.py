from django.http import HttpResponse

def index(request):
	return HttpResponse("est aes un prueba de la primera aplicacion")