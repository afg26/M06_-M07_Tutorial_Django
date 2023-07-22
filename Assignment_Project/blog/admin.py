from django.contrib import admin
from .models import Post, Comment
#imported the required libraries for the app 



#here we declare what we want to be shown while we open django admin page on the browser
admin.site.register(Post)
admin.site.register(Comment)
