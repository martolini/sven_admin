from django.db import models


class Category(models.Model):
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Categories"

class Question(models.Model):
	text = models.TextField()
	category = models.ForeignKey(Category)

	def __unicode__(self):
		return self.text

class Answer(models.Model):
	text = models.TextField()
	question = models.ForeignKey(Question)
	correct = models.BooleanField(default=False)

	def __unicode__(self):
		return self.text