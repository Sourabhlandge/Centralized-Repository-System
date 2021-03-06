"""CRS_MajorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from crs_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.crs_home_view),
    path('gov_schemes/', views.gov_schemes_view),
    path('gov_jobs/', views.gov_jobs_view),

    path('education_s_list/', views.education_list_view),
    path('health_s_list/', views.health_list_view),
    path('agriculture_s_list/', views.agriculture_list_view),
    path('electricity_s_list/', views.electricity_list_view),
    path('business_s_list/', views.business_list_view),
    path('youth_s_list/', views.youth_list_view),

    path('signup/', views.user_signup),
    path('logout/', views.logout),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact_us/', views.contact_us, name="contact_us"),

    # reset passwaord

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
