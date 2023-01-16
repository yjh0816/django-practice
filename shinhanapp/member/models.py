from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=128, verbose_name='이름')
    age = models.IntegerField(verbose_name='나이')

    class Meta:
        verbose_name= '회원'
        verbose_name_plural= '회원'
