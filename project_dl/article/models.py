from django.db import models

# Create your models here.
class Animal(models.Model):
    class Meta:
        db_table = "animal"
    animal_name = models.CharField(max_length=200)
    animal_desc = models.TextField()
    animal_price = models.IntegerField()
    animal_date = models.DateTimeField()


class Commands(models.Model):
    class Meta:
        db_table = 'comments'

    comment_text = models.TextField()
    comments_article = models.ForeignKey(Animal, on_delete=models.CASCADE)
