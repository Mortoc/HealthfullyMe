from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.signals import user_logged_in
from django.utils.timezone import now
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password

import hashlib
from datetime import timedelta

from core.timeutil import show_time_as

class HMUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=HMUserManager.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
class LoginInfo(models.Model):
    id = models.AutoField(primary_key=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    timestamp = models.DateTimeField(default=now)
    
    def __unicode__(self):
        return show_time_as(self.timestamp, 'UTC')


class HMUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
        db_index=True,
    )

    created_date = models.DateTimeField(default=now)
    
    first_name = models.CharField(default="", max_length=128)
    last_name = models.CharField(default="", max_length=128)
    
    logins = models.ManyToManyField(LoginInfo)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    receives_newsletter = models.BooleanField(default=False)
    is_legacy = models.BooleanField(default=False) # is this user imported from ROI Health

    objects = HMUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    
    def password_admin_reset(self):
        html = "<span>********&nbsp&nbsp&nbsp&nbsp<a href='/admin/tools/reset-password/" + self.email + "'>reset</a></span>";
        return mark_safe(html)
    
    password_admin_reset.allow_tags = True
    password_admin_reset.short_description = "Password"
    
# SingleUserUrl a key for a url that's tied to a single user account
class UserAccessCode(models.Model):
    @staticmethod
    def create(user, expires=now() + timedelta(weeks=1)):
        
        hash = hashlib.sha1()
        hash.update(user.email + settings.SECRET_KEY + show_time_as(now(), "UTC"))
        
        return UserAccessCode(
            code = hash.hexdigest(),
            user = user,
            valid_until = expires
        )
        
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=40, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_date = models.DateTimeField(default=now)
    valid_until = models.DateTimeField(null=True, blank=True)


def add_login_info(sender, user, request, **kwargs):
    login_info = LoginInfo(user=user)
    login_info.save()
    
    user.logins.add( login_info )
    user.save()

user_logged_in.connect(add_login_info)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    line1 = models.CharField(max_length=256)
    line2 = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=64, null=True, blank=True)

    def __unicode__(self):
        if self.line2 and self.line2 != " ":
            return "{0}\n{1}\n{2}\n{3}, {4}\n{5}\n{6}".format(self.name, self.line1, self.line2, self.city, self.state, self.zip, self.country)
        else:
            return "{0}\n{1}\n{2}, {3}\n{4}\n{5}".format(self.name, self.line1, self.city, self.state, self.zip, self.country)
        
    def html(self):
        return self.__unicode__().replace("\n", "<br />")
    