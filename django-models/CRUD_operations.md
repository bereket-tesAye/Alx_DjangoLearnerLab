# CRUD Operations for Book Model

This document demonstrates all CRUD (Create, Retrieve, Update, Delete) operations for the `Book` model in the `bookshelf` app.

---

## 1. Create

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Output: <Book: 1984 by George Orwell (1949)>
