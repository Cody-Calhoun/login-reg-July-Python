from django.db import models
# import re


class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be 2 characters or more"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be 2 characters or more"
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
