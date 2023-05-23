from django.shortcuts import render, redirect
from base.models import Charges
from .forms import ChargesForm

def charges(request):
    certs = Charges.objects.all()
    context = {'certs':certs, 'tabletitle':'Charges'.upper()}
    return render(request, 'charges/charges.html', context)

def add_charge(request):
    form = ChargesForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('charges')
    return render(request, 'charges/add-charge.html', {'form':form})

def update_charge(request,pk):
    charge = Charges.objects.get(id=pk)
    form = ChargesForm(request.POST or None, instance=charge)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('charges')
    return render(request, 'charges/update-charge.html', {'form':form}) 

def delete_charge(request, pk):
    charge = Charges.objects.get(id=pk)
    charge.delete()
    return redirect('charges')