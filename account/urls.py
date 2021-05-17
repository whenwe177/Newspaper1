from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    #path("password_change/",views.passwordChange,name="passwordChange"),
    #path("password_change/done/",views.passwordChangeDone,name="passwordChangeDone"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),name="password_change_complete"),
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"),name="password_change"),
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name="password_reset"),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name="password_reset_complete"),
]