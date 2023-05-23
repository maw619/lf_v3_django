from django.shortcuts import render, redirect
from base.models import Certifications
from .forms import CertificationForm

def certifications(request):
    certs = Certifications.objects.all()
    context = {'certs':certs, 'tabletitle':'certifications'.upper()}
    return render(request, 'certifications/certifications.html', context)

def add_cert(request):
    form = CertificationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('certifications')
    return render(request, 'certifications/add-cert.html', {'form':form})

def update_cert(request,pk):
    cert = Certifications.objects.get(id=pk)
    form = CertificationForm(request.POST or None, instance=cert)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('certifications')
    return render(request,'certifications/update-cert.html', {'form':form})

def delete_cert(request,pk):
    cert = Certifications.objects.get(id=pk)
    cert.delete()
    return redirect('certifications')
