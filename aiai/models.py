from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=70) #max length per CL
    description = models.CharField(max_length=100) #max_length per CL
    store_number = models.CharField(max_length=6) #enough for 999,999 stores.
    date_created = models.DateTimeField(auto_now_add = True)
    image_file = models.ImageField(upload_to='items/')
    
    def __unicode__(self):
        return self.name

class Store(models.Model):
    store_number = models.CharField(max_length=6)
    region = models.CharField(max_length=25) #max_length per CL
    pause_between_post = models.CharField(max_length=5) #in seconds. 
    pause_before_publish = models.CharField(max_length=5) #in seconds
    phone_number = models.CharField(max_length=40) #will allow for extension numbers
    manager_name = models.CharField(max_length=255) #store manager name
    ficticious_name = models.CharField(max_length=20) #Mr. Blue ?!
    email = models.EmailField() #email acct. used for posting
    
    def __unicode__(self):
        return self.store_number
        

class Demo(models.Model):
    name = models.CharField(max_length=255) #name of person requesting demo.
    email = models.EmailField() #person's email address
    phone_number = models.CharField(max_length=40) #allows for extension numbers.
    
    def __unicode__(self):
        return self.name