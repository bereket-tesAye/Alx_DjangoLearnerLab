from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms

# -------------------------------
# Book Form
# -------------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# -------------------------------
# Add Book View
# -------------------------------
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

# -------------------------------
# Edit Book View
# -------------------------------
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

# -------------------------------
# Delete Book View
# -------------------------------
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})


# -------------------------------
# Role check functions
# -------------------------------
def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'profile') and user.profile.role == 'Member'

# -------------------------------
# Views with access control
# -------------------------------
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


#authentication views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

@method_decorator(require_POST, name='dispatch')
class LogoutPostOnlyView(LogoutView):
    next_page = 'login'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add books related to the library
        context['books'] = self.object.books.all()
        return context

from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return  render(request, 'relationship_app/list_books.html', {'books':books})

def profiles(request):
    return render(request, 'relationship_app/profiles.html', {})


