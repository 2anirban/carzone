from django.db import models

#photo,first_name,last_name

#class Pages:
#def __init__(self,photo,first_name,last_name,designation,facebook_link,twitter_link,created_date):
#self.photo=photo


class Team(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='photos/%y/%m/%d')
    facebook_link=models.URLField(max_length=255)
    twitter_link=models.URLField(max_length=255)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name+ " "+self.last_name
