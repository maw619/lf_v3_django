from django.shortcuts import render,redirect
from base.models import EmailGroup, Employee
from .forms import AddEmailGroupForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def email_groups(request):
    email_groups = EmailGroup.objects.all()
    employee = Employee.objects.all()
    members_emails = []  
    members_emails2 = []  
    for x in employee:
        print(x.email)

    for z in email_groups:
        members_emails2.append(z.members.all())

    for email_group in email_groups:
        for member in email_group.members.all():
            members_emails.append(member.email) 

    form = AddEmailGroupForm()
    if request.method == 'POST': 
        form = AddEmailGroupForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('email_groups')
        
    context = {'email_groups': email_groups, 'members_emails':employee, 'form':form}
    return render(request, 'emailgroups/email-group.html', context)

def update_email_group(request,pk):
    email_group = EmailGroup.objects.get(id=pk)
    form = AddEmailGroupForm(instance=email_group)
    if request.method == 'POST':
        form = AddEmailGroupForm(request.POST, instance=email_group)
        if form.is_valid():
            form.save()
            return redirect('email_groups')
    context = {'form':form}
    return render(request, 'emailgroups/email-group-update.html', context)


def delete_email_group(request,pk):
    email_group = EmailGroup.objects.get(id=pk)
    email_group.delete()
    return redirect('email_groups')
