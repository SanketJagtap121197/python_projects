from django.shortcuts import render, HttpResponse # HttpResponse is used to send the response to the user (we imported HttpResponse Explicitly)

# Create your views here.
def index(request):
    context = { 
        'variable' : "this is sent",
        'variable1' : "Hello this is Sanket"
    }  # context is set of variables which is sent to template
       # context os a python dictionary
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage") # This is the response that will be sent to the user when the user visits the home page. (This is the function that we made in views.py file of home app)

def about(request):
    return HttpResponse("This is about page") # This is the response that will be sent to the user when the user visits the about page. (This is the function that we made in views.py file of home app)

def services(request):
    return HttpResponse("This is services page") # This is the response that will be sent to the user when the user visits the services page. (This is the function that we made in views.py file of home app)

def contact(request):
    return HttpResponse("This is contact page")