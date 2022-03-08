# serializers.py
from rest_framework import serializers
from .models import TestReq
from .models import Teacher

class TestReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReq
        fields = '__all__'


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "jobtitle", "profile", "avatar")
