from django.shortcuts import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import generic

from account.models import User
from .froms import PostForm
from .models import Post


def home(request):
    context = {
        'objects': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class user_post(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'objects'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)


class detail(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


class createview(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:userpost', kwargs={'username': self.request.user
                                                })

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class updateview(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'blog/create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class delete(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = '/blog/'
    template_name = 'blog/delete_view.html'
#
#
# def detail(request, pk):
#     context = {
#         'object': Post.objects.get(id=pk)
#     }
#     return render(request, 'blog/detail.html', context)
#
#
# @login_required
# def createview(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.author = request.user
#             obj.save()
#
#         return redirect('blog:home')
#     context = {
#         'form': form
#     }
#     return render(request, 'blog/create.html', context)


# @login_required
# def updateview(request, pk):
#     obj = Post.objects.get(id=pk)
#     form = PostForm(request.POST or None, instance=obj)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('blog:home')
#     context = {
#         'form': form,
#
#     }
#     return render(request, 'blog/create.html', context)


# @login_required
# def delete(request, pk):
#     obj = Post.objects.get(id=pk)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('blog:home')
#     return render(request, 'blog/delete_view.html', {'object': obj})


# def user_post(request, username):
#     object = Post.objects.filter(author__username=username)
#
#     return render(request, 'blog/home.html', {'objects': object})
