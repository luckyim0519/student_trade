from django.shortcuts import render

def home_views(request):
    #print(args,kwargs)
    #print(request.user) #to check which user is it
    #return HttpResponse('<h1>HELOO</h1>')
    return render(request, 'start_page/default.html')
    
