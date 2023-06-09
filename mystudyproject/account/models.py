from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserAdded(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth = models.DateField(blank=True, null=True) #blank-是否允许空值；null-空值的时候填入null
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    address = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)

    def __str__(self):
        return 'user:{}'.format(self.user.username)