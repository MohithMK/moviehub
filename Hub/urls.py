from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('signup/',views.signup, name = 'signup'),
    path('login/', views.logins, name = 'login'),
    path('', views.home, name = 'home'),
    path('logout/', views.logout_view, name='logout'),
    path('MovieDetail/<id>', views.movie_detail, name='moviedetail'),
    path('UserList/', views.user_list,name='userlist'),
    path('MovieList/', views.MovieView,name='movielist'),
    path('UserUpdate/<str:pk>/', views.user_update, name='userupdate'),
    path('MovieUpdate/<str:pk>/', views.movie_update, name='movieupdate'),
    path('thanks/', views.thanks, name='thanks'),
    path('checkout/', views.checkout, name='checkout'),
    path('failed/', views.failed, name='failed'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'),name= "password_change"),
    path('change_password_done/', auth_views.PasswordChangeDoneView .as_view(template_name='password_change_done.html'),name="password_change_done"),
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

]