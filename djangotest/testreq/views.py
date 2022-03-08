from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
import faker, json
from django.middleware.csrf import get_token
from rest_framework import viewsets
from .models import TestReq
from .serializers import TestReqSerializer
from django.middleware.csrf import get_token

# Create your views here.

def get_csrf_token(request):   
    csrf_token = get_token(request)  # 获取csrf_token的值
    return JsonResponse({'token': csrf_token})

class ResViewSet(viewsets.ModelViewSet):
    queryset = TestReq.objects.all()
    serializer_class = TestReqSerializer

fake = faker.Faker(locale='zh_CN') # 初始化，指定生成中文格式数据
def create_phone():
    """生成电话"""
    phones = [fake.phone_number() for _ in range(5)] 
    return " ".join(phones)


def phone(request):

    data = create_phone()
    return HttpResponse(data)

def create_id(num):
    """生成身份证"""
    identity_ids = [fake.ssn() for i in range(int(num))]
    return " ".join(identity_ids)

@require_http_methods(['GET', 'POST'])
def id(request):
    print(request)
    print(type(request))
    num = request.POST.get("num")  # 如果"Content-type"="application/x-www-form-urlencoded"
    # num = json.loads(request.body).get("num") # 如果"Content-type"="application/json"
    # number = request.args.get("num")
    # num = request.GET['num']
    # num = request.GET.get("num")
    print(num)
    # print(number)
    # print(request.GET)
    if num == "" or num is None:
        data1 = create_id(5)
    else:
        data1 = create_id(num)
    return HttpResponse(data1)


def create_name(num):
    """生成姓名"""
    names = [fake.name() for i in range(int(num))] 
    return " ".join(names)


def name(request):
    num = request.GET.get("num")
    print(num)
    if num == "" or num is None:
        data = create_name(20)
    else:
        data = create_name(num)
    return HttpResponse(data)# Create your views here.