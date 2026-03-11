from django.http import HttpResponse

def home(request):
    return HttpResponse("Shrestha says Hello!")

