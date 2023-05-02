from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from account.forms import LoginForm, UserUpdateForm, ProfileUpdateForm, RegisterForm


def register_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'created')
            return redirect('account:login')
    else:
        form=RegisterForm()
    return render(request,'account/login.html',{'form':form})

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('blog:home')
            else:
                messages.error(request, 'there is nothing in here ')

    return render(request, 'account/login.html', {'form': form})


@login_required
def logoutview(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("blog:home")


def ProfileView(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        pro_form = ProfileUpdateForm(request.POST,
                                     request.FILES,
                                     instance=request.user.profile)
        if user_form.is_valid() and pro_form.is_valid():
            user_form.save()
            pro_form.save()
            return redirect('account:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        pro_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': pro_form
    }
    return render(request, 'account/profile.html', context)
