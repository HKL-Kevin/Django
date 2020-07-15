from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32)

class Book(models.Model):
    name = models.CharField(max_length=32)
    detail = models.CharField(max_length=255)
    publisher = models.ForeignKey("Publisher",on_delete=models.PROTECT)
    author = models.ManyToManyField("Author")
    """
    on_delete参数取值
        modles.CASCAE   级联删除
        modles.PROTECT  保护
        modles.SET(V)   设置为V值
        modles.SETDEFAULT   删除后设置为默认值
        modles.SETNULL  设置为NULL
    """

class Author(models.Model):
    name = models.CharField(max_length=32)