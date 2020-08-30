from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Map_wc
import csv
import pandas as pd

# wheelchair.csv 파일 pandas로 불러오기
with open('C:\DJANGOexam\mapservice\map\Seoul_wheelchair.csv', 'r', encoding='utf-8') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []

for i in range(len(s)):
    st = (s['x'][i], s['y'][i], s['info'][i], s['tel'][i], s['location'][i])
    ss.append(st)
    # print(ss)
for i in range(len(s)):
    Map_wc.objects.create(x=ss[i][0], y=ss[i][1], info=ss[i][2], tel=ss[i][3], location=ss[i][4])
# print(ss[0][0], ss[0][1], ss[0][2], ss[0][3], ss[0][4])
# 경도가 x 위도가 y. 젠장

def w_map(request):
    w_maplist = Map_wc.objects.all()
    context = {"w_maplist" : w_maplist}
    return render(request, 'mapservice.html', context)
