from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# adminside uploadportfolio................................
class Portfoliopage(models.Model):
    img = models.ImageField( )
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    class Meta:
        db_table = "Portfoliopage"
    def __str__(self):
        return self.title

# adminside uploadproject......................................
class Uploadproject(models.Model):
    name = models.CharField(max_length=50)
    img1 = models.FileField(null=True)
    img2 = models.ImageField(null=True)
    img3 = models.ImageField(null=True)
    img4 = models.ImageField(null=True)
    img5 = models.ImageField(null=True)
    img6 = models.ImageField(null=True)
    img7 = models.ImageField(null=True)
    img8 = models.ImageField(null=True)
    img9 = models.ImageField(null=True)
    img10 = models.ImageField(null=True)
    img11 = models.ImageField(null=True)
    img12 = models.ImageField(null=True)
    img13 = models.ImageField(null=True)
    img14 = models.ImageField(null=True)
    img15 = models.ImageField(null=True)
    title = models.CharField(max_length=1000)
    discription = models.CharField(max_length=1000)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Uploadproject"

# adminside contact page information...............................
class Personaldetail(models.Model):
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=11)
    email  = models.EmailField()
    class Meta:
        db_table = "Personaldetail"



# clientside contact form..........................................
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20)
    class Meta:
        db_table = "Contacts"
    def __str__(self):
        return self.name
