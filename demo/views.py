from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from demo.models import Student


def hello(request):
    return HttpResponse("hello world")


# 返回
def hello2(request):
    return HttpResponse("<h1>hello world</h1>")

# 返回templates
def hello3(request):
    return render(request,'hello.html')

def home(request):
    return render(request,'home.html')

# 添加demo_student  http://127.0.0.1:8000/demo/add/
def add(request):
    student = Student()
    student.s_name = 'laughing2'
    student.save()
    return HttpResponse('Add Success')

# 查询
def select(request):
    students = Student.objects.all()
    for student  in students:
        print(student.s_name)
    context={
        "students":students
    }
    return render(request,'student.html',context=context)

# 修改
# http://127.0.0.1:8000/demo/update/
def update(request):
    student = Student.objects.get(pk = 1)
    student.s_age = 10000
    student.save()
    return HttpResponse('update Success')

# 删除
# http://127.0.0.1:8000/demo/delete/
def delete(request):
    student = Student.objects.get(pk = 2)
    student.delete()
    return HttpResponse('delete Success')













