from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} عزیز ثبت نام شما با موفقیت انجام شد. لطفا وارد شوید")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@receiver(user_logged_in)
def on_user_logged_in(request, user, **kwargs):
    messages.success(request, f"{user.username} عزیز خوش آمدید")


@receiver(user_logged_out)
def on_user_logged_out(request, user, **kwargs):
    messages.success(request, f"{user.username} عزیز  شما با موفقیت خارج شدید")


@login_required
def profile(request, **kwargs):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"{request.user} عزیز حساب کاربری شما با موفقیت بروز رسانی شد")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
