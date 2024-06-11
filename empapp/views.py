from django.shortcuts import render ,redirect,HttpResponse,get_object_or_404
from .models import employee , department

# Create your views here.
def listemployee(request):
    employees=employee.objects.all()
    departments=department.objects.all()
    return render(request,"empapp/list.html",{"employees":employees,"departmnets":departments})
def addemployee(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        empcode = request.POST.get("empcode")
        phone = request.POST.get("phone")
        department = request.POST.get("department")
        
        if name and empcode and phone and department:
            employee.objects.create(
                name=name,
                empcode=empcode,
                phone=phone,
                department=department
            )
            return redirect("listemployee")
        else:
            return HttpResponse("NOT SUCCESSFUL")
    return render(request, "empapp/new.html")


def editemployee(request, empcode):
    emp = get_object_or_404(employee, empcode=empcode)
    
    if request.method == "POST":
        name = request.POST.get("name")
        empcode = request.POST.get("empcode")
        phone = request.POST.get("phone")
        department = request.POST.get("department")
        
        if name and empcode and phone and department:
            emp.name = name
            emp.empcode = empcode
            emp.phone = phone
            emp.department = department
            emp.save()
            return redirect("listemployee")
        else:
            return HttpResponse("NOT SUCCESSFUL")
    
    return render(request, "empapp/edit.html", {"emp": employee})

def delemployee(request,empcode):
    user=get_object_or_404(employee,empcode=empcode)
    user.delete()
    return redirect ("listemployee")