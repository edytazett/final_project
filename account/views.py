from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from account.forms import LoginForm, SignInForm


# Create your views here.

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login_register.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)
            return redirect('main_page')
        return render(request, 'login_register.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main_page')


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'login_register.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('main_page')
        return render(request, 'login_register.html', {'form': form})
