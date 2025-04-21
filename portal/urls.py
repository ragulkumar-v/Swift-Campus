from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('complaint', views.complaint, name='complaint'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('staff/', views.staff, name='staff'),
    path('logout/', views.logout, name='logout'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('resolve_complaint/<int:complaint_id>/', views.resolve_complaint, name='resolve_complaint'),
    path('withdraw/<str:complaint_id>/', views.withdraw_complaint, name='withdraw_complaint'),
    path('FAQ/', views.faq, name='faq'),
    path('About Us/', views.about, name='about'),
    path('Report-Issue/', views.report_issue, name='report_issue'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
    template_name='password_form.html',
    email_template_name='password_email.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_complete.html'), name='password_reset_complete'),
]
