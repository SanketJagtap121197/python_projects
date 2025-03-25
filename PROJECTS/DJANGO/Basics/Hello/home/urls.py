from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [  # "" is blank path, it means the home page
    path("", views.index, name='home'),  # This is the URL configuration for the home app, we made explicitly. (If this path matches then send the request to home.urls)
    path("about", views.about, name='about'),  # This is the URL configuration for the about page of the home app, we made explicitly. (If this path matches then send the request to home.urls)
    path("services", views.services, name='services'),  # This is the URL configuration for the services page of the home app, we made explicitly. (If this path matches then send the request to home.urls) 
    path("contact", views.contact, name='contact'), # This is the URL configuration for the contact page of the home app, we made explicitly. (If this path matches then send the request to home.urls)
    # Then make functions (of index and about and also if there are any further functions) in views.py file of home app to handle these requests.
]

# Remember if we made a path here but not a function in views.py file of home app to handle that request then it will show an error, i.e. 'home.views' does not have any attribute 'xyz' (xyz is the function that we made in urls.py file of home app but not in views.py file of home app)