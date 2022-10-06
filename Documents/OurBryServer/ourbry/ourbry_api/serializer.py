from rest_framework import serializers


class StudentMembersSerializer(serializers.Serializer):
    nis = serializers.CharField()
    name = serializers.CharField()
    gender = serializers.CharField()
    status = serializers.CharField()
    first_fmd = serializers.CharField()
    second_fmd = serializers.CharField()
