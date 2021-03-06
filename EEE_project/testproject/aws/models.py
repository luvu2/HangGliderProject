from django.db import models
import json

# Create your models here.
class token(models.Model):
    text =  models.CharField(max_length=10)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.text



# 기본 단어 및 수어 영상이 담긴 Model
class Basic(models.Model):
    location = models.CharField(default='' , max_length=100)
    ref_word = models.CharField(null=True, max_length=20)
    mean = models.TextField(null=True)
    part = models.CharField(max_length=10, default='')
    word = models.CharField(max_length=20, null=True, blank=True)

    def set_ref_word(self, x):
        self.ref_word = json.dumps(x)

    def get_ref_word(self):
        return json.loads(self.ref_word)

    def __str__(self):
        return self.word

# 숫자 단어 및 수어 영상이 담긴 Model
class Number(models.Model):
    location = models.CharField(default='', max_length=100)
    ref_word = models.TextField(null=True)
    mean = models.TextField(null=True)
    part = models.CharField(max_length=10, default='')
    word = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.word

# 지화 단어 및 수어 영상이 담긴 Model
class Finger(models.Model):
    location = models.CharField(default='', max_length=100)
    ref_word = models.TextField(null=True)
    mean = models.TextField(null=True)
    part = models.CharField(max_length=10, default='')
    word = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.word
