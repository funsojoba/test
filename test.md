1. CRUD Operations with Django ORM

	•	Task: Create a Django management command that performs basic CRUD operations on a Book model.
	•	Model:

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()


	•	Requirements:
	•	Create 5 books in the database.
	•	Retrieve all books with titles starting with “A”.
	•	Update the author of one specific book.
	•	Delete books published before the year 2000.
•	Update the author of one specific book.
	•	Delete books published before the year 2000.
	•	Expected Output: Logs of each operation (e.g., books created, updated, or deleted).





2. Custom Django Middleware

	•	Task: Write a custom middleware that logs the time taken to process a request and the status code of the response.
	•	Requirements:
	•	Log the details in the console or a file.
	•	Handle both normal requests and error scenarios.
	•	Expected Output: Logs like INFO: Time taken: 0.123s, Status: 200.



3. Django Form with Validation

	•	Task: Create a form to register users with fields for:
	•	Username (required, unique).
	•	Email (required, valid format).
	•	Password (required, minimum 8 characters).
	•	Requirements:
	•	Use Django’s forms.Form or forms.ModelForm.
	•	Add custom validation for email to ensure it contains @example.com.
	•	Render the form in a simple HTML template.
	•	Expected Output: A working form with error messages displayed for invalid inputs.


Template Filtering and Rendering

	•	Task: Display a list of products on a template with a price filter.
	•	Model:

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

	•	Requirements:
	•	Create a view that fetches all products with prices below a value passed in the query parameter (?max_price=100).
	•	Render the filtered products on a template.
	•	Handle cases where no products match the criteria.