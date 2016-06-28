from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	book_id = models.AutoField(primary_key=True)
	borrower = models.CharField(max_length=200) 
	STATUS = (
		('B', 'Borrowed'),
		('O', 'Overdue'),
		('L', 'Lost'),
		('S', 'On Shelf'),
	)
	status = models.CharField(max_length=1, choices=STATUS)
	amount = models.IntegerField()

	def __unicode__(self):
		return self.title
	