from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm



# from blog.admin import Post
# Create your views here.
def index(request):
    #List all posts
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        # return render(request, 'blogs/index.html',{'posts': posts})
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('index')
    else:
        form = PostForm()

    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'blogs/index.html', context)


def about(request):
    return render(request, 'blogs/about.html',{})



