from django.shortcuts import render, redirect
from base.models import Employee, Cargo
from .forms import AddEmployeeForm

def employees(request):
    employees = Employee.objects.all()
    context = {'emps': employees, 'tabletitle': 'employees'.upper()}
    return render(request, 'employees/employees.html', context)

def employee_info(request, pk):
    emp = Employee.objects.get(id=pk)
    return render(request, 'employees/employee-info.html', {'emp': emp, 'tableTitle': 'employee info'.upper()})

def add_employee(request):
    form = AddEmployeeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('employees')
    return render(request, 'employees/add-employee.html',{'form':form})

def update_employee(request, pk):
    emp_by_id = Employee.objects.get(id=pk)
    form = AddEmployeeForm(request.POST or None,instance=emp_by_id)
    if form.is_valid():
        form.save()
        return redirect('employees')
    return render(request, 'employees/update-employee.html', {'form':form})

def delete_employee(request,pk):
    emp_by_id = Employee.objects.get(id=pk)
    emp_by_id.delete()
    return redirect('employees')