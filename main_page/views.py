from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, user. You're at the main index.")