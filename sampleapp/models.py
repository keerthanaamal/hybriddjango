from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Registration(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()

class Student2023(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Student2022(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    class Meta:
        db_table="my table"

class Employee(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class  Employeepoints(models.Model):
    empid=models.ForeignKey(Employee,on_delete=models.CASCADE)
    points=models.IntegerField()


class Registrationfile(models.Model):
    name=models.CharField(max_length=30)
    regfile=models.FileField(upload_to="media")


    
class testing(models.Model):
    image_lawn=models.ImageField(upload_to='images/')
    phone=models.IntegerField(null=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    
    
class Trainer(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()