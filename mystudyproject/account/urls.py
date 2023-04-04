from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('login2/', auth_views.LoginView.as_view(template_name='account\login2.html'), name='login2'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('register/', views.registration, name='register'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='account/password_change.html',
                                               success_url='/account/password_change_done/'),
         name='password_change'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),
                name='password_change_done'),
    path('selfinfo/', views.self_info, name='selfinfo'),
    path('selfinfo_edit/', views.selfinfo_edit, name='selfinfo_edit'),
    path('selfimage_edit/', views.selfimage_edit, name='selfimage_edit')
]