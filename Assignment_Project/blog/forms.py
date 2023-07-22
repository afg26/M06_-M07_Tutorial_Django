from django import forms
from .models import Post, Comment
#imported the required libraries for the app 


#declaring our forms that we will using and we attach these forms to the models.py so that we can attach it to the database.
#for this app we have two forms:
#one for adding a post 
#one for adding a comment.
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)