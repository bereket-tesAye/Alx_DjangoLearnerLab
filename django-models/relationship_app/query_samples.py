from relationship_app.models import Author, Book, Library, Librarian    

#  Option 1: Using author instance
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)

# Option 2: Query directly by author name
books_by_author = Book.objects.filter(author__name="John Doe")
# Option 1: Using library instance
library = Library.objects.get(name="City Library")
books_in_library = library.books.all()

# Option 2: Query directly
books_in_library = Book.objects.filter(library__name="City Library")
# Option 1: Using library instance
library = Library.objects.get(name="City Library")
librarian = library.librarian

# Option 2: Query directly
librarian = Librarian.objects.get(library__name="City Library")
s