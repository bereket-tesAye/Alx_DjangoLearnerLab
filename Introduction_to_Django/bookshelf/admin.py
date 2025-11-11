from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable search by title or author
    search_fields = ('title', 'author')
    
    # Add filters for publication year
    list_filter = ('publication_year',)

# Register with the custom admin configuration
admin.site.register(Book, BookAdmin)
