from django.shortcuts import render  
from .forms import UserRegistration
from .models import user
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    form=UserRegistration()
    stu=user.objects.all()
    return render (request, 'index.html' , {'form':form , 'stu':stu})

# insert data
# @csrf_exempt
def save_data(request):
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            sid=request.POST.get('stuid')
            nm=request.POST['name']
            email=request.POST['email']
            if(sid == ""):    
                usr=user.objects.create(email=email, name=nm)
            else:
                usr=user(id = sid , email=email, name=nm)
            usr.save()
            stud=user.objects.values()
            stud_data=list(stud)
            return JsonResponse({'status':'save', 'stud_data':stud_data})
            
        else:
            return JsonResponse({'status':'0'})

# delete data
def delete_data(request):
    if request.method == "POST":
        id=request.POST.get('sid')
        pi=user.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

#  EDIT OR Update Data
def edit_data(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        student=user.objects.get(pk=id)
        student_data={
            "id":student.id,
            "name":student.name,
            "email":student.email
        }
        return JsonResponse(student_data)