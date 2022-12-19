from django.urls import path
from .views import BookListCreateView,BookDetailView
urlpatterns = [
    path('',BookListCreateView.as_view(),name='Book_list_create'),
    path('<int:pk>',BookDetailView.as_view(),name='Book_detail'),

    
]