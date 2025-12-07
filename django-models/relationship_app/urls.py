from . import views
from django.urls import path
from django.urls import path
from .views import LibraryDetailView

#authintication views
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    path('', views.list_books, name = 'list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    #login
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    
    # Logout
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Registration
    path("register/", RegisterView.as_view(), name="register"),

    path('accounts/profile/', views.profiles, name='profile'),

    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),
]
