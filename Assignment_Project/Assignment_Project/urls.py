
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
#imported the required libraries for the app 




#here we define the urls that we will use while we navigate through the webpage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
]
