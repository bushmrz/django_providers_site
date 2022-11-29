from django.urls import path
from .views import HomePage, Register, Login, LogOutUser, ForgetPassword, ChangePassword


urlpatterns = [
    path('home/', HomePage, name='home-page'),
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', LogOutUser, name='logout'),
    path('reset/', ForgetPassword, name='forgotPass'),
    path('change-password/<token>/' , ChangePassword , name="change_password"),
    path('', Login, name='test')
    
]
