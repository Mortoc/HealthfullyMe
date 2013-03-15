from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.signals import user_logged_in
from django.utils.timezone import now

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
    is_admin = models.BooleanField(default=False)
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

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




def add_login_info(sender, user, request, **kwargs):
    login_info = LoginInfo(user=user)
    login_info.save()
    
    user.logins.add( login_info )
    user.save()


user_logged_in.connect(add_login_info)




class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True)
    line1 = models.CharField(max_length=256)
    line2 = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=256, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=8)
    country = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        if self.line2:
            return "{0}\n{1}\n{2}\n{3}, {4}\n{5}\n{6}".format(self.name, self.line1, self.line2, self.city, self.state, self.zip, self.country)
        else:
            return "{0}\n{1}\n{2}, {3}\n{4}\n{5}".format(self.name, self.line1, self.city, self.state, self.zip, self.country)
    