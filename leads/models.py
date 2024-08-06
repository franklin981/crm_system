from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# AbstractUser, is a subset of AbstractBaseUser
# using this is poor, its always best to create ur own user models as recommended from django and customize it to ur taste
# User = get_user_model()

class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) # This is a many to one relation, means we will have an agent associated with the lead of that role
    #setting on_delete = :
    #CASCADE means when u delete the Agent filed, u want the lead to be deleted too
    #.SET_NULL means the lead => agent column will be set as empty and also where we set attribute null=True
    #.SET_DEFAULT means the lead => agent column will be set to the default, where we set the default= to be something we want as a default 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # means for every agent table, we can only have one user
    
    def __str__(self):
        return f"{self.user.first_name}"