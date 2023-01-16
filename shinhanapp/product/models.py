from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='상품명')
    content = models.TextField(verbose_name='상품내용')
    price = models.IntegerField(verbose_name='가격')
    location = models.CharField(max_length=256, verbose_name='위치')

    def __str__(self):
        return f"{self.title}: {self.price}원"
        
    class Meta:
        db_table = 'shinhan_project'
        verbose_name= '상품'
        verbose_name_plural= '상품'
