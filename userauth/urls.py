from django.urls import path
from . import views
from django.contrib.auth import views as authViews
from .forms import LoginForm

app_name = 'userauth'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    
    path('login/', authViews.LoginView.as_view(
        template_name = 'userauth/login.html',
        authentication_form = LoginForm
    ), name='login'),

    path('logout/', authViews.LogoutView.as_view(), name='logout'),

]