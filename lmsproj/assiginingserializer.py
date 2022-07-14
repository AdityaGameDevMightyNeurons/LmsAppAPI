from rest_framework import serializers
from lmsproj.models import AssigningUser





class AssigningUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssigningUser
        fields = ("batch","course","activeModule","student","teacher")
