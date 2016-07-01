from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	book_id = models.AutoField(primary_key=True)
	borrower = models.CharField(max_length=200) 
	STATUS = (
		('On Shelf', 'On Shelf'),
		('Borrowed', 'Borrowed'),
		('Overdue', 'Overdue'),
		('Lost', 'Lost'),
	)
	status = models.CharField(max_length=10, choices=STATUS)
	amount = models.IntegerField()

	def __unicode__(self):
		return self.title
	