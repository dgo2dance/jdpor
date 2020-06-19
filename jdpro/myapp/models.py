# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 这是和数据库中的myapp_jd数据表相对应的模型字段
class MyappJd(models.Model):
    goods_id = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    detail_url = models.CharField(max_length=250)
    goodrate = models.CharField(db_column='goodRate', max_length=250)  # Field name made lowercase.
    pic_url = models.CharField(max_length=250)
    types = models.CharField(max_length=250)
    '''下面是10天的字段设置，db_column=3.05的意思就是，这个字段在数据库中的名字是3.05'''
    number_3_05 = models.CharField(db_column='3.05', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_06 = models.CharField(db_column='3.06', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_07 = models.CharField(db_column='3.07', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_08 = models.CharField(db_column='3.08', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_09 = models.CharField(db_column='3.09', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_10 = models.CharField(db_column='3.10', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_11 = models.CharField(db_column='3.11', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_12 = models.CharField(db_column='3.12', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_13 = models.CharField(db_column='3.13', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_14 = models.CharField(db_column='3.14', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_15 = models.CharField(db_column='3.15', max_length=250)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    max_today = models.CharField(db_column='max/today', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'myapp_jd'   #这里是设置模型字段在数据库中的名字

# 这是用户表，用户存储用户信息的
class HhhhUser(models.Model):
    objects = models.Manager()
    """用户表"""
    # 性别设置
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)    # 名字字段，max_length是此最长字数是多少
    password = models.CharField(max_length=256) # 密码字段
    email = models.EmailField(unique=True)  # 邮箱字段
    sex = models.CharField(max_length=32, choices=gender, default="男")  # 性别字段
    jifen = models.IntegerField(default="0")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

