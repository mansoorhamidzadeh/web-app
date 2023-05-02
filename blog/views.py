from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .froms import PostForm
from .models import Post


def home(request):
    context = {
        'objects': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


@login_required
def detail(request, pk):
    context = {
        'object': Post.objects.get(id=pk)
    }
    return render(request, 'blog/detail.html', context)


@login_required
def createview(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()

        return redirect('blog:home')
    context = {
        'form': form
    }
    return render(request, 'blog/create.html', context)


@login_required
def updateview(request, pk):
    obj = Post.objects.get(id=pk)
    form = PostForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    context = {
        'form': form,

    }
    return render(request, 'blog/create.html', context)


@login_required
def delete(request, pk):
    obj = Post.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('blog:home')
    return render(request, 'blog/delete_view.html', {'object': obj})


def user_post(request, username):
    object = Post.objects.filter(author__username=username)

    return render(request, 'blog/home.html', {'objects': object})
