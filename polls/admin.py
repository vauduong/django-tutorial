from django.contrib import admin

# Register your models here.
from .models import Question

#Registering a model lets Django know that it should be displayed on the index page
admin.site.register(Question)