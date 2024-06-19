from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Event, About
from .forms import CommentForm

class EventsList(generic.ListView):
    model = Event
    template_name = "index.html"
    paginate_by = 12

def event_detail(request, event_id):
    queryset = Event.objects.all()
    event = get_object_or_404(Event, id=event_id)  
    return render(
        request,
        "events/event_detail.html",
        {"event": event}
    )

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()
    
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            },
            )

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
