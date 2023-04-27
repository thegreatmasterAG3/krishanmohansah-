from django.db import models

# Create your models here.


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class CV(models.Model):
    pdf_file = models.FileField(upload_to='cv/')
