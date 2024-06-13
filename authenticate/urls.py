from django.urls import path
from authenticate import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login/',views.login_user, name='login'),
  path('logout_user/',views.logout_user, name='logout'),
  path('register_user/',views.register_user, name='register'),
  path('profile_user/',views.profile_user, name='profile'),
  path('edit_profile_user/',views.edit_profile, name='edit_profile_user'),
  path('change_password/', views.change_password, name='change_password'),
  path('contact/',views.contact,name='contact'),

  path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name="reset_password"),
  path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name="password_reset_done"),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
  path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
         name="password_reset_complete"),
] 
