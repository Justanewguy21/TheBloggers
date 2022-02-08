from django.urls import path
from django.contrib.auth import views as  auth_views

from .views import sign_up 


urlpatterns = [
    path('sign_up/', sign_up, name = 'members-sign-up' ),
    #path('login/', auth_views.LogoutView.as_view(template_name ='members/login.html'), name = 'member-login' ),
    path('', auth_views.LoginView.as_view(template_name ='members/login.html'), name = 'member-login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name ='members/logout.html'), name = 'member-logout' )
    
] 
