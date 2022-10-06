import MySQLdb
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ourbry_api.models import StudentMember
from ourbry_api import serializer
from django.core import serializers
from django.http import HttpResponse


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def show_api(request):
    name = request.POST.get('name', 'No')
    nis = request.POST.get('nis', 'No')
    gender = request.POST.get('gender', 'No')
    first_fmd = request.POST.get('first_fmd', 'No')
    second_fmd = request.POST.get('second_fmd', 'No')
    status = "success"
    message = "All data is successfully"

    # convert string to binary
    # https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
    first_fmd = first_fmd.encode("utf-8")
    second_fmd = second_fmd.encode("utf-8")

    # import to database
    try:
        student_members = StudentMember.objects.create(nis=nis, name=name, gender=gender, status="1",
                                                       first_fmd=first_fmd,
                                                       second_fmd=second_fmd)
    except IndentationError:
        status = "failed"
        message = "Double Entry on Primary Key"

    except:
        print("another error")

    return Response({"info": status,
                     "message" : message,
                     "data": {"name": name,
                              "nis": nis,
                              }})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def absen_student_members(request):
    data = StudentMember.objects.all()
    # data_json = serializers.serialize('json', data)
    # return HttpResponse(data_json, content_type="application/json")
    data_serializer = serializer.StudentMembersSerializer(data, many=True)
    return Response(data_serializer.data)
