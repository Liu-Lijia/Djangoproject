from django.db import models

# Create your models here.
class TestReq(models.Model):
    content = models.TextField()

class Teacher(models.Model):
	title = models.CharField(max_length=100)
	profile = models.TextField()  # 简介
	avatar = models.URLField()  # 图像