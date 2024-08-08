import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Author, Publisher, Book, Store

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        # Create Authors
        authors_data = [
            {"name": "J.K. Rowling", "age": 58},
            {"name": "George R.R. Martin", "age": 75},
            {"name": "Stephen King", "age": 76},
            {"name": "Agatha Christie", "age": 85},
            {"name": "J.R.R. Tolkien", "age": 81},
            {"name": "Ernest Hemingway", "age": 61},
            {"name": "Mark Twain", "age": 74},
            {"name": "Jane Austen", "age": 41},
            {"name": "Charles Dickens", "age": 58},
            {"name": "F. Scott Fitzgerald", "age": 44},
        ]
        authors = [Author.objects.create(**data) for data in authors_data]

        # Create Publishers
        publishers_data = [
            "Bloomsbury Publishing",
            "Bantam Books",
            "Scribner",
            "HarperCollins",
            "Penguin Books",
        ]
        publishers = [Publisher.objects.create(name=name) for name in publishers_data]

        # Create Books
        books_data = [
            {"name": "Harry Potter and the Philosopher's Stone", "pages": 223, "price": Decimal("19.99"), "rating": 4.8,
             "publisher": publishers[0]},
            {"name": "A Game of Thrones", "pages": 694, "price": Decimal("29.99"), "rating": 4.7,
             "publisher": publishers[1]},
            {"name": "The Shining", "pages": 447, "price": Decimal("24.99"), "rating": 4.5, "publisher": publishers[2]},
            {"name": "Murder on the Orient Express", "pages": 256, "price": Decimal("14.99"), "rating": 4.6,
             "publisher": publishers[3]},
            {"name": "The Hobbit", "pages": 310, "price": Decimal("22.99"), "rating": 4.7, "publisher": publishers[0]},
            {"name": "The Old Man and the Sea", "pages": 132, "price": Decimal("11.99"), "rating": 4.3,
             "publisher": publishers[4]},
            {"name": "Adventures of Huckleberry Finn", "pages": 366, "price": Decimal("18.99"), "rating": 4.4,
             "publisher": publishers[2]},
            {"name": "Pride and Prejudice", "pages": 279, "price": Decimal("15.99"), "rating": 4.6,
             "publisher": publishers[3]},
            {"name": "Great Expectations", "pages": 505, "price": Decimal("21.99"), "rating": 4.5,
             "publisher": publishers[1]},
            {"name": "The Great Gatsby", "pages": 180, "price": Decimal("13.99"), "rating": 4.4,
             "publisher": publishers[4]},
            {"name": "Harry Potter and the Chamber of Secrets", "pages": 251, "price": Decimal("19.99"), "rating": 4.8,
             "publisher": publishers[0]},
            {"name": "Harry Potter and the Prisoner of Azkaban", "pages": 317, "price": Decimal("19.99"), "rating": 4.8,
             "publisher": publishers[0]},
            {"name": "Harry Potter and the Goblet of Fire", "pages": 636, "price": Decimal("29.99"), "rating": 4.8,
             "publisher": publishers[0]},
            {"name": "Harry Potter and the Order of the Phoenix", "pages": 766, "price": Decimal("29.99"),
             "rating": 4.8, "publisher": publishers[0]},
            {"name": "Harry Potter and the Half-Blood Prince", "pages": 607, "price": Decimal("29.99"), "rating": 4.8,
             "publisher": publishers[0]},
            {"name": "Harry Potter and the Deathly Hallows", "pages": 607, "price": Decimal("29.99"), "rating": 4.8,
             "publisher": publishers[0]},
            {"name": "A Clash of Kings", "pages": 768, "price": Decimal("29.99"), "rating": 4.7,
             "publisher": publishers[1]},
            {"name": "A Storm of Swords", "pages": 973, "price": Decimal("29.99"), "rating": 4.7,
             "publisher": publishers[1]},
            {"name": "A Feast for Crows", "pages": 753, "price": Decimal("29.99"), "rating": 4.6,
             "publisher": publishers[1]},
            {"name": "A Dance with Dragons", "pages": 1016, "price": Decimal("29.99"), "rating": 4.6,
             "publisher": publishers[1]},
            {"name": "The Dark Tower: The Gunslinger", "pages": 224, "price": Decimal("19.99"), "rating": 4.5,
             "publisher": publishers[2]},
            {"name": "The Dark Tower II: The Drawing of the Three", "pages": 400, "price": Decimal("19.99"),
             "rating": 4.5, "publisher": publishers[2]},
            {"name": "The Dark Tower III: The Waste Lands", "pages": 512, "price": Decimal("19.99"), "rating": 4.5,
             "publisher": publishers[2]},
            {"name": "The Dark Tower IV: Wizard and Glass", "pages": 887, "price": Decimal("19.99"), "rating": 4.5,
             "publisher": publishers[2]},
            {"name": "The Dark Tower V: Wolves of the Calla", "pages": 931, "price": Decimal("19.99"), "rating": 4.5,
             "publisher": publishers[2]},
            {"name": "The Dark Tower VI: Song of Susannah", "pages": 432, "price": Decimal("19.99"), "rating": 4.5,
             "publisher": publishers[2]},
            {"name": "The Dark Tower VII: The Dark Tower", "pages": 845, "price": Decimal("19.99"), "rating": 4.5,
             "publisher": publishers[2]},
            {"name": "And Then There Were None", "pages": 272, "price": Decimal("14.99"), "rating": 4.6,
             "publisher": publishers[3]},
            {"name": "The Murder of Roger Ackroyd", "pages": 312, "price": Decimal("14.99"), "rating": 4.6,
             "publisher": publishers[3]},
            {"name": "The ABC Murders", "pages": 272, "price": Decimal("14.99"), "rating": 4.6,
             "publisher": publishers[3]},
            {"name": "The Lord of the Rings: The Fellowship of the Ring", "pages": 423, "price": Decimal("22.99"),
             "rating": 4.7, "publisher": publishers[0]},
            {"name": "The Lord of the Rings: The Two Towers", "pages": 352, "price": Decimal("22.99"), "rating": 4.7,
             "publisher": publishers[0]},
            {"name": "The Lord of the Rings: The Return of the King", "pages": 416, "price": Decimal("22.99"),
             "rating": 4.7, "publisher": publishers[0]},
            {"name": "The Sun Also Rises", "pages": 251, "price": Decimal("15.99"), "rating": 4.3,
             "publisher": publishers[4]},
            {"name": "For Whom the Bell Tolls", "pages": 480, "price": Decimal("18.99"), "rating": 4.4,
             "publisher": publishers[4]},
            {"name": "The Adventures of Tom Sawyer", "pages": 274, "price": Decimal("14.99"), "rating": 4.4,
             "publisher": publishers[2]},
            {"name": "Sense and Sensibility", "pages": 226, "price": Decimal("15.99"), "rating": 4.6,
             "publisher": publishers[3]},
            {"name": "Emma", "pages": 474, "price": Decimal("17.99"), "rating": 4.6, "publisher": publishers[3]},
            {"name": "David Copperfield", "pages": 882, "price": Decimal("21.99"), "rating": 4.5,
             "publisher": publishers[1]},
            {"name": "A Tale of Two Cities", "pages": 489, "price": Decimal("18.99"), "rating": 4.5,
             "publisher": publishers[1]},
            {"name": "The Beautiful and Damned", "pages": 464, "price": Decimal("16.99"), "rating": 4.4,
             "publisher": publishers[4]},
            {"name": "Tender Is the Night", "pages": 317, "price": Decimal("15.99"), "rating": 4.4,
             "publisher": publishers[4]},
            {"name": "This Side of Paradise", "pages": 305, "price": Decimal("14.99"), "rating": 4.3,
             "publisher": publishers[4]},

        ]
        books = []
        for i in range(50):
            book_data = books_data[i % len(books_data)].copy()  # Cycle through the provided book data
            book_data["name"] = f"{book_data['name']} - Edition {i+1}"  # Make each book name unique
            book_data["pubdate"] = timezone.now().date() - timezone.timedelta(days=random.randint(0, 3650))
            book = Book.objects.create(**book_data)
            book.authors.set(random.sample(authors, k=random.randint(1, 3)))
            books.append(book)

        # Create Stores
        stores_data = [
            "BookStore A",
            "BookStore B",
            "BookStore C",
            "BookStore D",
            "BookStore E",
        ]
        stores = [Store.objects.create(name=name) for name in stores_data]

        # Add books to stores
        for store in stores:
            store.books.set(random.sample(books, k=random.randint(5, 15)))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))