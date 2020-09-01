from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Map_wc
import csv, folium, json
import pandas as pd
from django.core import serializers

# # wheelchair.csv 파일 불러오기
# with open('C:\DJANGOexam\mapservice\map\Seoul_wheelchair.csv', 'r', encoding='utf-8') as f:
#     dr = csv.DictReader(f)
#     s = pd.DataFrame(dr)
#     # print(s)

def w_map(request):
    mapwheelchair = Map_wc.objects.all()
    context = {"mapwheelchair" : mapwheelchair}
    return render(request, 'mapservice.html', context)

def getApi(request):
    report = Map_wc.objects.all()
    report_list = serializers.serialize('json',report)
    return HttpResponse(report_list, content_type="text/json_comment-filtered")

def mapTest(request):
    return render(request, 'mapTest.html')

# ss = []
# for i in range(len(s)):
#     st = (s['x'][i], s['y'][i], s['info'][i], s['tel'][i], s['location'][i])
#     ss.append(st)
#     print(ss)

# for i in range(len(s)):
#    Map_wc.objects.create(x=ss[i][0], y=ss[i][1], info=ss[i][2], tel=ss[i][3], location=ss[i][4])
# # print(ss[0][0], ss[0][1], ss[0][2], ss[0][3], ss[0][4])

