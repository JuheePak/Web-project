from django.db import models
import os
from django.conf import settings

# class Map_all(models.Model):
#     address = models.CharField(max_length=30) # 주소
#     x = models.IntegerField() # 위도
#     y = models.IntegerField() # 경도
#     info = models.CharField(max_length=30) # 상세정보
#     tel = models.CharField(max_length=30) # 전화번호

class Map_wc(models.Model):
    x = models.CharField(max_length=30) # 위도
    y = models.CharField(max_length=30) # 경도
    info = models.CharField(max_length=30)  # 상세정보
    tel = models.CharField(max_length=30) # 전화번호
    location = models.CharField(max_length=40) # 장소명