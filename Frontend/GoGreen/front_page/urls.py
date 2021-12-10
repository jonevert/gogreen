from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/overview
    path('', views.index, name="frontpage-index"),
    path('register', views.register, name="register-index"),
    path('login', LoginView.as_view(template_name='front_page/login.html'), name='login-index'),
    path('logout', LogoutView.as_view(next_page='login-index'), name='logout-index'),
    path('about_us', views.about, name="about-index"),
    path('docs', views.docs, name="docs-index"),
]