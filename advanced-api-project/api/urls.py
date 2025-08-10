from django.urls import path
from . import views

urlpatterns = [
    # Standard CRUD endpoints with pk in URL
    path('books/', views.ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
    path('books/create/', views.CreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', views.UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.DeleteView.as_view(), name='book-delete'),

    # Your no-PK endpoints
    path('books/update/', views.BookUpdateNoPKView.as_view(), name='book-update-no-pk'),
    path('books/delete/', views.BookDeleteNoPKView.as_view(), name='book-delete-no-pk'),
]
