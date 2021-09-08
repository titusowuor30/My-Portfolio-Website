from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='about')
    bio=models.TextField(default='my bio here')
    image=models.ImageField(upload_to='media/images/',blank=True,null=True)
    cv=models.FileField(upload_to='media/cv/',blank=True,null=True)
    phone=models.CharField(max_length=15,default="+254743793901")

    def __str__(self):
        return self.user.username

class service(models.Model):
    title = models.CharField(max_length=100)
    icon=models.CharField(max_length=255,blank=True,null=True)
    content = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class skill(models.Model):
        title = models.CharField(max_length=100)
        percnt=models.IntegerField(default=50)

        def __str__(self):
            return self.title

class experience(models.Model):
        title = models.CharField(max_length=100)
        percnt=models.IntegerField(default=50)

        def __str__(self):
            return self.title


class team(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/teams/',blank=True,null=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class SkillsDesc(models.Model):
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.description

class ExpDesc(models.Model):
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.description

class LeftMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255,default='example@gmail.com')
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=255)

    def __str__(self):
        return self.name