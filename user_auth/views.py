from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Create your views here.
# 가입정보 입력화면은 user_register_page
def user_register_page(request):
    return render(request, 'user_register.html')
