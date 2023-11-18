from django.db import models

# first register model in admin.py
# after that register app in settings.py
# then run command python manage.my makemigrations
# after that run command python manage.py migrate -> this will create table in database
# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name