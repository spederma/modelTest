# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    # id = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=30) # 设置字段类型的， varchar

    class Meta:
        verbose_name = '作者' # 复数
        verbose_name_plural = verbose_name

    # py2.x
    def __unicode__(self):
        return self.name

    # py3.x
    # def __str__(self):
    #     pass


class AuthorInfo(models.Model):
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    addr = models.CharField(max_length=30)
    birthday = models.DateField()
    author = models.OneToOneField('Author') # 信息模型和作者对应，一对一的对应

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    addr = models.CharField(max_length=40)
    city = models.CharField(max_length=10)
    state_province = models.CharField(max_length=20)
    website = models.CharField(max_length=30)

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    publish_date = models.DateField()
    publisher = models.ForeignKey('Publisher') # 书和出版社的一对多关系
    author = models.ManyToManyField('Author') # 作者和书的多对多关系