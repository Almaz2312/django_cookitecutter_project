from django.views import generic
from .models import Project


class ProjectIndexView(generic.ListView):
    model = Project
    context_object_name = "projects"
    template_name = "project_index.html"


class ProjectDetailView(generic.DetailView):
    model = Project
    context_object_name = "project"
    template_name = "project_detail.html"
