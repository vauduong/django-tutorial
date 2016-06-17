from __future__ import unicode_literals

#changing models
#Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.


from django.db import models
#models contain fields and behaviors
# Create your models here.

#subclasses models.Model
#variables represent database fields, database column name
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    #ForeignKey tells Django that each Choice is related to a Question, defines relationship

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
