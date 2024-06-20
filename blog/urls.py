from django.urls import path
from . import views

urlpatterns = [
    # Blog post URLs
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

    # Event URLs
    path('events/', views.EventsList.as_view(), name='events_home'),  # Changed the name to avoid conflict
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]
