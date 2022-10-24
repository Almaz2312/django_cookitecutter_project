from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Category, Comment, Post
from .forms import CommentForm


class BlogIndexView(generic.ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog_index.html"


class BlogCategoryView(generic.ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog_category.html"

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs["category"])
        return Post.objects.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super(BlogCategoryView, self).get_context_data(**kwargs)
        context["category"] = self.category
        return context


class BlogDetailView(generic.FormView, generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog_detail.html"
    form_class = CommentForm
    success_url = "#"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comment"] = Comment.objects.filter(post=self.get_object()).oreder_by("-created_on")

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=self.get_object()
            )
            comment.save()

        return super().form_valid(form)
