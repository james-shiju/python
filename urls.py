from django.urls import path
from . import views

# the app_name addition will need the namespace from the link in the view
# error in above will give you following error
# Error during template rendering : 'simpleapp' is not a registered namespace
# app_name = 'demo'

# Url patterns below for the app
urlpatterns = [
    # ex: /demo/
    path('', views.index, name='index'),
    
]
