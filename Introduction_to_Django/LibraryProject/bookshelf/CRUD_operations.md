# CRUD Operations Summary for the Book Model

This file documents all Create, Retrieve, Update, and Delete operations performed on the `Book` model using the Django shell.

---

## ✅ Create Operation

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>
