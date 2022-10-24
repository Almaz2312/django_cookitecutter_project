from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='blog_index'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('category:<category>/', views.BlogCategoryView.as_view(), name='blog_category'),
]
