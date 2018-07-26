from django.http import HttpResponse

def index(request):
	#return HttpResponse("est aes un prueba de la primera aplicacion")
	return render(
    request,
    'index.html',
     context={'num_books':"num_books",'num_instances':"num_instances",'num_instances_available':"num_instances_available",'num_authors':"num_authors"},
)