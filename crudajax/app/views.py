from django.shortcuts import render
from app.models import StudentData
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def HomePage(request):
    students=StudentData.objects.all()
    return render(request,'home/home.html',{"students":students})
@csrf_exempt
def InsertStudent(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    gender = request.POST.get("gender")
    try:
        student=StudentData(name=name,email=email,gender=gender)
        student.save()
        student_data={"id":student.id,"created_at":student.created_at,"error":False,"errormessage":"student Added successfully"}
        return JsonResponse(student_data,safe=False)
    except:
        student_data={"error":True,"errormessage":"Failed to Add studentdata"}
        return JsonResponse(student_data,safe=False)

@csrf_exempt
def UpdateStudent(request):
    data = request.POST.get("data")
    dict_data = json.loads(data)
    try:
        for dic_single in dict_data:
            student = StudentData.objects.get(id=dic_single['id'])
            student.name = dic_single['name']
            student.email = dic_single['email']
            student.gender = dic_single['gender']
            student.save()
        stuent_data = {"error": False, "errorMessage": "Updated Successfully"}
        return JsonResponse(stuent_data, safe=False)
    except:
        stuent_data = {"error": True, "errorMessage": "Failed to Update Data"}
        return JsonResponse(stuent_data, safe=False)

@csrf_exempt
def delete_data(request):
    id=request.POST.get("id")
    try:
        student=StudentData.objects.get(id=id)
        student.delete()
        student_data={"error":False,"errormessage":"delete successful"}
        return JsonResponse(student_data,safe=False)
    except:
        student_data={"error":True,"errormessage":"failed to delete data"}
        return JsonResponse(student_data,safe=False)

