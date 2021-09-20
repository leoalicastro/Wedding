from django.db import models
import re
import bcrypt
from .models import *
from datetime import datetime


class UserManager(models.Manager):
    def validator(self,post_data):
        errors = {}
        if len(post_data['fname']) < 2:
            errors['fname'] = "First name must be atleast 2 characters"
        if len(post_data['lname']) < 2:
            errors['lname'] = "Last name must be atleast 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Email format invalid"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be atleast 8 characters"
        if post_data['password'] != post_data['confirm']:
            errors['confirm'] = "Passwords don't match"
        if len(User.objects.filter(email = post_data['email'])) > 0:
            errors['email'] = "Email already exists"
        return errors
    def edit_validator(self, post_data):
        errors = {}
        if len(post_data['fname']) < 2:
            errors['fname'] = "First name must be atleast 2 characters"
        if len(post_data['lname']) < 2:
            errors['lname'] = "Last name must be atleast 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Email format invalid"
        if len(User.objects.filter(email = post_data['email'])) > 0:
            errors['email'] = "Email already exists"
        return errors
    def login_validator(self, post_data):
        errors={}
        LoginUser = User.objects.filter(email = post_data['logemail'])
        if len(LoginUser) > 0:
            if bcrypt.checkpw(post_data['logpassword'].encode(), LoginUser[0].password.encode()):
                print('match')
            else:
                errors['logpassword'] = "Password is incorrect"
        else:
            errors['logemail'] = "Email does not exist"
        return errors

class WeddingManager(models.Manager):
    def validator(self,post_data):
        errors = {}
        if len(post_data['sfname']) < 2:
            errors['sfname'] = "Spuse's first name must be atleast 2 characters"
        if len(post_data['slname']) < 2:
            errors['slname'] = "Spouse's last name must be atleast 2 characters"
        if len(post_data['caddress']) < 4:
            errors['caddress'] = "Adress must contain atleast 4 characters"
        if len(post_data['ccity']) < 4:
            errors['ccity'] = "City must contain atleast 2 characters"
        ZIP_REGEX = re.compile(r'^[0-9]{5}(?:-[0-9]{4})?$')
        if not ZIP_REGEX.match(post_data['czip']):
            errors['czip'] = "Zip format invalid"
        if len(post_data['raddress']) < 4:
            errors['raddress'] = "Adress must contain atleast 4 characters"
        if len(post_data['rcity']) < 4:
            errors['rcity'] = "City must contain atleast 2 characters"
        if not ZIP_REGEX.match(post_data['czip']):
            errors['czip'] = "Zip format invalid"
        if datetime.strptime(post_data['cdate'], '%Y-%m-%d') < datetime.now():
            errors['cdate'] = 'Ceremony Date should be in the future'
        if datetime.strptime(post_data['rdate'], '%Y-%m-%d') < datetime.now():
            errors['rdate'] = 'Reception Date should be in the future'
        return errors
    def edit_validator(self,post_data):
        errors = {}
        if len(post_data['sfname']) < 2:
            errors['sfname'] = "Spuse's first name must be atleast 2 characters"
        if len(post_data['slname']) < 2:
            errors['slname'] = "Spouse's last name must be atleast 2 characters"
        if len(post_data['caddress']) < 4:
            errors['caddress'] = "Adress must contain atleast 4 characters"
        if len(post_data['ccity']) < 4:
            errors['ccity'] = "City must contain atleast 2 characters"
        ZIP_REGEX = re.compile(r'^[0-9]{5}(?:-[0-9]{4})?$')
        if not ZIP_REGEX.match(post_data['czip']):
            errors['czip'] = "Zip format invalid"
        if len(post_data['raddress']) < 4:
            errors['raddress'] = "Adress must contain atleast 4 characters"
        if len(post_data['rcity']) < 4:
            errors['rcity'] = "City must contain atleast 2 characters"
        if not ZIP_REGEX.match(post_data['rzip']):
            errors['rzip'] = "Zip format invalid"
        if datetime.strptime(post_data['cdate'], '%Y-%m-%d') < datetime.now():
            errors['cdate'] = 'Ceremony Date should be in the future'
        if datetime.strptime(post_data['rdate'], '%Y-%m-%d') < datetime.now():
            errors['rdate'] = 'Reception Date should be in the future'
        return errors

class CreditManager(models.Manager):
    def validator(self,post_data):
        errors = {}
        Credit_REGEX = re.compile(r'^[0-9]')
        if not Credit_REGEX.match(post_data['card_number']):
            errors['card_number'] = "Credit card format invalid"
        if len(post_data['card_number']) < 15:
            errors['card_number'] = "Credit card number must contain atleast 15 characters"
        if len(post_data['card_number']) > 16:
            errors['card_number'] = "Credit card number must not exceed 16 characters"
        ZIP_REGEX = re.compile(r'^[0-9]{5}(?:-[0-9]{4})?$')
        if not ZIP_REGEX.match(post_data['card_zip']):
            errors['card_zip'] = "Zip format invalid"
        if datetime.strptime(post_data['card_date'], '%Y-%m-%d') < datetime.now():
            errors['card_date'] = 'Card has expired'
        return errors

class RegistryManager(models.Manager):
    def validator(self,post_data):
        errors = {}
        if len(post_data['funame']) < 2:
            errors['funame'] = "Fund name must contain atleast 2 characters"
        if len(post_data['funame']) > 50:
            errors['funame'] = "Fund name must not exceeed 50 characters"
        if ['amount'] > ['remaining_balance']:
            errors['amount'] = "Amount must be less than remaining balance"
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Wedding(models.Model):
    sfname = models.CharField(max_length=255)
    slname = models.CharField(max_length=255)
    cvenue = models.CharField(max_length=255, null=True)
    caddress = models.CharField(max_length=255)
    ccity = models.CharField(max_length=255)
    cstate = models.CharField(max_length=255)
    cdate = models.DateField()
    ctime = models.TimeField()
    czip = models.IntegerField(null=True)
    rvenue = models.CharField(max_length=255, null=True)
    raddress = models.CharField(max_length=255)
    rcity = models.CharField(max_length=255)
    rstate = models.CharField(max_length=255)
    rdate = models.DateField(null=True)
    rzip = models.IntegerField(null=True)
    rtime = models.TimeField()
    image = models.ImageField(upload_to='weddings', null=True)
    description = models.CharField(max_length=1000, null=True)
    wedding_owner = models.ForeignKey('User', related_name="wedding_created", on_delete=models.CASCADE, null=True)

    objects = WeddingManager()

class Registry(models.Model):
    funame = models.CharField(max_length=255, null=True)
    goal = models.IntegerField(null=True)
    remaining_balance = models.IntegerField(null=True)
    registry_owner = models.ForeignKey('User', related_name="registry_created", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = RegistryManager()

class Credit(models.Model):
    amount = models.IntegerField()
    card_number = models.IntegerField(null=True)
    card_date = models.DateField(null=True)
    card_zip = models.IntegerField(null=True)
    message = models.CharField(max_length=255)
    credit_owner = models.ForeignKey('User', related_name="credit_created", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = CreditManager()

class Post(models.Model):
    post = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey('User', related_name="posts_uploaded", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField('User', related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
