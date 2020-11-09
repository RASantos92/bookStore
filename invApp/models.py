from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=255)
	desc = models.TextField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Author(models.Model):
	firstName = models.CharField(max_length=45)
	lastName = models.CharField(max_length=45)
	books = models.ManyToManyField(Book, related_name="publishers")
	notes = models.TextField(max_length=255, null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
