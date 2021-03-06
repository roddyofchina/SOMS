# -*- coding:utf8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField(max_length=244, verbose_name=u'用户')
    audit_time = models.DateTimeField(auto_now_add=True, verbose_name=u'时间')
    type = models.CharField(max_length=10, verbose_name=u'类型')
    action = models.CharField(max_length=20, verbose_name=u'动作')
    action_ip = models.CharField(max_length=15, verbose_name=u'用户IP')
    content = models.TextField(verbose_name=u'内容')

    class Meta:
        ordering = ['-audit_time']
        verbose_name = u'审计信息'
        verbose_name_plural = u'审计信息管理'

class UserCommandGroup(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
        verbose_name=u'命令别名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'远程命令分组'
        verbose_name_plural = u'远程命令分组管理'

class UserCommand(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
        verbose_name=u'命令别名')
    command = models.TextField(blank=True, verbose_name=u'系统命令')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'远程命令'
        verbose_name_plural = u'远程命令管理'

class UserDirectory(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name=u'目录别名')
    directory = models.TextField(blank=True, verbose_name=u'系统目录')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'远程目录'
        verbose_name_plural = u'远程目录管理'

