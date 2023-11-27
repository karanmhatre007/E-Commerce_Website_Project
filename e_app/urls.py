"""
URL configuration for e_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('about/',v.about,name='about'),
    path('contact/',v.contact,name='contact'),
    path('category/<slug:val>',v.CategoryView.as_view(),name='category'),
    path('category-title/<val>',v.CategoryTitle.as_view(),name='category-title'),
    path('product-detail/<int:pk>',v.ProductDetail.as_view(),name='product-detail'),
    path('profile/',v.ProfileView.as_view(),name='profile'),


    #login authentication
    path('registration',v.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('pasword-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
