from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer
from .permissions import OwnerOnly

class BookListCreateView(ListCreateAPIView):
    
    queryset=Book.objects.all()
    serializer_class=BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[OwnerOnly]