# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the existing book
book = Book.objects.get(id=1)

# Delete the book
book.delete()
# Expected output:
# (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Expected output:
# <QuerySet []>
