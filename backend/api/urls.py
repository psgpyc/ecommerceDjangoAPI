from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='api_home'),
    path('publishers/', views.PublisherListView.as_view(), name='api_publishers'),
    path('publishers/<int:pk>', views.PublisherDetailView.as_view(), name='api_publisher_detail'),
]