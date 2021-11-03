from django import forms
from .models import Post 

#To input post
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = Post
        fields = ('title','content')
