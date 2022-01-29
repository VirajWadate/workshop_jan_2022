from django.http import HttpResponse

def index(request):
	return HttpResponse("Deployed applicatino on GCP server")