from django.db import models

# Create your models here.

class Verification(models.Model):
     name=models.CharField( max_length=50)
     serial_no = models.IntegerField(default=0)
     contact_number = models.IntegerField(default=0)
     contact_email = models.EmailField(max_length=254)
     personel = models.IntegerField(default=0)
     

class Worker(models.Model):
     fname = models.CharField(max_length=50)
     lname = models.CharField(max_length=50)
     profile_pic = models.ImageField(upload_to='profilePics/', height_field=None, width_field=None, max_length=None,default='DEFAULT_VALUE')
     bio = models.TextField(max_length= 100)
     skills = models.ManyToManyField('Skills')
     Verify = models.ForeignKey("Verification",  on_delete=models.CASCADE)
     rating = models.IntegerField(default=0)     

     def __str__(self):
          return "%s The Help from %s" % (self.lname, self.bureau)


class Client(models.Model):
     fname = models.CharField(max_length=50)
     lname = models.CharField(max_length=50)
     profile_pic = models.ImageField(upload_to='profilePics/', height_field=None, width_field=None, max_length=None,default='DEFAULT_VALUE')
     # home_address=  models.ForeignKey("Location", on_delete=models.CASCADE)

class Skills(models.Model):
     name = models.CharField( max_length=30)

class Client_gig(models.Model):
     description=models.CharField( max_length=50) 
     skills_required = models.ManyToManyField("Skills")
     client = models.ForeignKey("Client", on_delete=models.CASCADE)

class Worker_gig(models.Model):
     description=models.CharField( max_length=50) 
     skills_required = models.ManyToManyField("Skills")
     client = models.ForeignKey("Client", on_delete=models.CASCADE)

class Categories(models.Model):
     pass
class Project(models.Model):
     pass

    
class Reviews(models.Model):
     review = models.TextField(max_length=100)
     client = models.ForeignKey("Client", on_delete=models.CASCADE)

