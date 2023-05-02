from django.db import models

# Create your models here.


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CV(models.Model):
    pdf_file = models.FileField(upload_to='cv/')

class IMAGE(models.Model):
    img_krish1 = models.ImageField()
    img_krish2 = models.ImageField()
    img_testi1 = models.ImageField()
    img_testi2 = models.ImageField()

class TEXT(models.Model):
    logo = models.TextField()
    home1 = models.TextField()
    home2 = models.TextField()
    home3 = models.TextField()
    about1 = models.TextField()
    about2 = models.TextField()
    about3 = models.TextField()
    about4 = models.TextField()
    about_name = models.TextField()
    about_email = models.TextField()
    about_linkedin = models.TextField()
    about_instagram = models.TextField()
    skill1 = models.TextField()
    skill2 = models.TextField()
    skill3 = models.TextField()
    skill4 = models.TextField()
    skill5 = models.TextField()
    testi0 = models.TextField()
    testi1 = models.TextField()
    testi1_1 = models.TextField()
    testi1_2 = models.TextField()
    testi2 = models.TextField()
    testi2_1 = models.TextField()
    testi2_2 = models.TextField()
    contact_loc = models.TextField()
    contact_get = models.TextField()
    contact_link = models.TextField()
    last1 = models.TextField()
    last2 = models.TextField()
    last3 = models.TextField()


class LINK(models.Model):
    github = models.TextField()
    linkedin = models.TextField()
    instagram = models.TextField()
    facebook = models.TextField()
    location = models.TextField()


class TITLE(models.Model):
    title = models.TextField()