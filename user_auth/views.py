from django.shortcuts import redirect, render

# Create your views here.

def login(self):
    return render(self, 'login.html', name='login')

def logout(self):
    redirect('home')

def signup(self):
    return render(self, 'signup.html', name='signup')

def change_pwd(self):
    return render(self, 'forget_password.html', name="change")
