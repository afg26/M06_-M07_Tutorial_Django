from django.apps import AppConfig
##imported the required libraries for the app 

#here we make our class for the application and we name it also.
#this is done by django-admin startapp <name of the app> and enter 
#we write the above command in the terminal when we first start our project.
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
