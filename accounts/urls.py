from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls')),
    path('register/', views.register, name='register'),
    path('see_request', views.see_request),
    path('user_info/', views.see_info),
    path('private_place', views.private_place),
    path('staff_place/', views.staff_place),
    path('add_message/', views.add_messages),
]
