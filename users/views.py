from django.shortcuts import render, redirect
from .forms import UserOurRegistration, ProfileImage, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан!Введите имя пользователя и пароль.')
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'}, )

@login_required
def profile(request):
    img_profile = ProfileImage()
    update_user = UserUpdateForm()
    data = {
        "img_profile": img_profile,
        "update_user": update_user
    }

    return render(request, 'users/profile.html', data)