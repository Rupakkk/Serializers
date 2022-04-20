from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
# Model Object - Single Student data
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    print(stu)
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')


 
# Query Set- All object data

def student_list(request):
    stu = Student.objects.all()
    serialize = StudentSerializer(stu,many=True) # We need to put many=True for more than one
    # json_data = JSONRenderer().render(serialize.data)
    # return HttpResponse(json_data,content_type='application/json') 
    # We can write the above two steps in one line like below using JsonResponse
    return JsonResponse(serialize.data,safe=False) # We need to put safe = False for non dictionary items