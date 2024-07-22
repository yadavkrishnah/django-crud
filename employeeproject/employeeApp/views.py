from django.shortcuts import render,redirect
from django.views import View
from employeeApp.models import employee

# Create your views here.
class home(View):
    def get(self,request):
        return render (request,'index.html')


class registerview(View):
    def get(self,request):
        return render (request,'register.html')
    
    def post(self,request):
        name=request.POST.get("name")
        salary=request.POST.get("salary")
        designation=request.POST.get("designation")
        email=request.POST.get("email")
        employee.objects.create(name=name,salary=salary,designation=designation,email=email)
        return redirect('home_view')
    

class employeelist(View):
    def get(self,request):
        emp=employee.objects.all()     # queryset
        return render(request,'emp_list.html',{'data':emp})

class deleteemployee(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        emp=employee.objects.get(id=id)
        emp.delete()
        return redirect('list_view')
    
class UpdateEmployee(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        emp=employee.objects.get(id=id)
        return render(request,'edit.html',{'data':emp})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=employee.object.get(id=id)
        name=request.POST.get("name")
        salary=request.POST.get("salaet")
        desig=request.POST.get("desigg")
        email=request.POST.get("email")
        emp.name=name
        emp.salary=salary
        emp.designation=desig
        emp.email=email
        emp.save()
        return redirect('list_view')




    
    