#when something is modified in the backend it sends a signal to a receiver and it invokes a side effect/custom function
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

def updateUser(sender, instance, **kwargs):
    user = instance 
    if user.email != '':
        user.username=user.email
    
pre_save.connect(updateUser, sender=User)
