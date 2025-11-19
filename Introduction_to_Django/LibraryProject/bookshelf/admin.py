from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 1. Columns shown in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # 2. Filters shown on the right-hand side
    list_filter = ('publication_year', 'author')

    # 3. Search box (top right)
    search_fields = ('title', 'author')

    # (Optional) default ordering
    ordering = ('title',)
