from django.urls import path
from . import views

urlpatterns = [
    path("announcements/", views.AnnouncementView.as_view(), name=""),
    path("faqs/", views.FaqView.as_view(), name=""),
    path("contact/", views.ContactView.as_view(), name=""),
    path("blogs/",views.BlogView.as_view(),name=""),
    path("team/", views.TeamView.as_view(), name=""),
    path('redis-test/', views.redis_test_view),
]
