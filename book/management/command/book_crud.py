from django.core.management.base import BaseCommand
from book.models import Book

class Command(BaseCommand):
    help = 'Performs CRUD operations on Book model'
    def handle(self, *args, **kwargs):
        # Create 5 books
        books = [
            {
                "title": "Art of war",
                "author": "Author 1",
                "published_date": "2022-01-01"
            },
            {
                "title": "RIch dad poor dad",
                "author": "Author 2",
                "published_date": "2022-02-01"
            },
            {
                "title": "Armonia",
                "author": "Author 3",
                "published_date": "2022-03-01"
            },
            {
                "title": "Book 4",
                "author": "Author 4",
                "published_date": "2022-04-01"
            },
            {
                "title": "Book 5",
                "author": "Author 5",
                "published_date": "1999-05-01"
            }
            
        ]
        
        try:
            for book in books:
                Book.objects.get_or_create(
                    title=book["title"], 
                    author=book["author"], 
                    published_date=book["published_date"])
                self.stdout.write(self.style.SUCCESS(f'Successfully created book: {book["title"]}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating book: {e}'))
            
        
        # retrieve all the books with title starting with "A"
        books = Book.objects.filter(title__startswith="A")
        self.stdout.write(self.style.SUCCESS(f'Retrieved books: '))
        for book in books:
            self.stdout.write(self.style.SUCCESS(f'{book.title} by {book.author} published on {book.published_date}'))
            
        # update the author of one specific book
        book_to_update = Book.objects.get(title="Armonia")
        book_to_update.author = "New Author"
        book_to_update.save()
        self.stdout.write(self.style.SUCCESS(f'Updated book: {book_to_update.title} by {book_to_update.author}'))
        
        # Delete books published before the year 2000.
        books_to_delete = Book.objects.filter(published_date__year__lt=2000)
        book_count = books_to_delete.count()
        books_to_delete.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {book_count} book(s)'))