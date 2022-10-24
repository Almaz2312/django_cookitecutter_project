from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProjectIndexView.as_view(), name="project_index"),
    path("<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail")
]
