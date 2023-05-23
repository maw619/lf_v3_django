from django.shortcuts import render, redirect
from base.models import Report, Photo, Photo2
from .forms import AddReportForm, AddPhotoForm, AddPhotoForm2
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import F
from PIL import Image
import io

@login_required(login_url='/login/')
def reports(request):
    reports = Report.objects.all() 
    # for report in reports:        
    #     for supervisor in report.supervisors.all():
    #         print(supervisor)
    context = {'reports': reports, 'tabletitle':'Reports'.upper()}
    return render(request, 'reports/reports.html', context)


@login_required(login_url='/login/')
def add_report(request):
    form = AddReportForm(request.POST or None, initial={'employee': request.user.username})
    if request.method == 'POST': 
        if form.is_valid():
            form.instance.rep_user_name = request.user.username
            form.save()
            return redirect('add_photo', pk=form.instance.id)
    return render(request, 'reports/add-report.html', {'form':form}) 

@login_required(login_url='/login/')
def update_report(request, pk):
    report_by_id = Report.objects.get(id=pk)
    form = AddReportForm(request.POST or None, instance=report_by_id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('reports')
    return render(request, 'reports/update-report.html', {'form':form})


@login_required(login_url='/login/')
def detailed_report(request, pk):
    request.session['rep_key'] = pk 
  
    report = Report.objects.get(id=pk)
    photo1 = Photo.objects.filter(reports_id=pk)
    photo2 = Photo2.objects.filter(reports2_id=pk)
    rep_desc = report.rep_desc
    rep_user_name = report.rep_user_name
    desc = report.rep_desc
    rep_notes = report.rep_notes
    rep_date = report.rep_date
    pr_desc = report.project.pr_desc
    supervisors = report.supervisors 
 
    context = {
        'rep_desc': rep_desc,
        'rep_user_name': rep_user_name,
        'desc': desc,
        'rep_notes': rep_notes,
        'rep_date': rep_date,
        'pr_desc':pr_desc,
        'supervisors':supervisors,
        'photo1':photo1,
        'photo2':photo2,
        'rep_key':request.session['rep_key'], 
    }

    return render(request, 'reports/detailed-report.html', context)

def delete_report(request, pk):
    report_by_id = Report.objects.get(id=pk)
    report_by_id.delete()
    return redirect('reports')






## PHOTOS =========== PHOTOS =========== PHOTOS =========== PHOTOS =========== PHOTOS =========== PHOTOS ##

MAX_IMAGE_SIZE = 1024
 


def compress_image(image):
    # Open the image using PIL
    img = Image.open(image)

    # Resize the image if necessary
    if img.size[0] > MAX_IMAGE_SIZE or img.size[1] > MAX_IMAGE_SIZE:
        img.thumbnail((MAX_IMAGE_SIZE, MAX_IMAGE_SIZE), Image.ANTIALIAS)

    # Create an in-memory buffer to save the image
    img_byte_array = io.BytesIO()

    # Save the image to the buffer with the original format or JPEG format with compression
    if img.format == 'PNG':
        img.save(img_byte_array, format='PNG', optimize=True)
    else:
        img.save(img_byte_array, format='JPEG', optimize=True, quality=80)

    # Rewind the buffer and replace the image file
    img_byte_array.seek(0)
    image.file = img_byte_array




def add_photo(request, pk): 
    form = AddPhotoForm(request.POST, request.FILES or None) 
    if request.method == 'POST':
        if form.is_valid():
            photo = form.save(commit=False)  # Get the unsaved photo instance
            photo.ph_user_name = request.user.username
            photo.reports_id = pk  # Assign the desired value to the reports field
            compress_image(photo.ph_link) 
            photo.save()  # Save the photo instance to the database
            return redirect('detailed_report', pk)
    context = {'form':form}
    return render(request, 'reports/add-photo.html',context)

def add_photo2(request, pk, ph1_id): 
    form = AddPhotoForm2(request.POST, request.FILES or None) 
    if request.method == 'POST':
        if form.is_valid():
            photo = form.save(commit=False)  # Get the unsaved photo instance
            photo.ph_user_name = request.user.username
            photo.reports2_id = pk  # Assign the desired value to the reports field
            photo.photo_id = ph1_id
            compress_image(photo.ph_link2) 
            photo.save()  # Save the photo instance to the database
            return redirect('detailed_report', pk = request.session['rep_key'])
    context = {'form':form}
    return render(request, 'reports/add-photo.html',context)

def update_photo1(request, pk):
    photo1 = Photo.objects.get(id=pk)
    form = AddPhotoForm(request.POST or None, request.FILES or None, instance=photo1)
    if request.method == 'POST': 
        if form.is_valid():
            form.save(commit=False)
            compress_image(photo1.ph_link) 
            form.save()
            return redirect('detailed_report', request.session['rep_key'])
    context = {'form':form, 'img': photo1.ph_link}
    return render(request, 'reports/update-photo.html', context)

def update_photo2(request, pk):
    photo2 = Photo2.objects.get(id=pk)
    form = AddPhotoForm2(request.POST or None, request.FILES or None, instance=photo2)
    if request.method == 'POST': 
        if form.is_valid():
            form.save(commit=False)
            compress_image(photo2.ph_link2) 
            form.save()
            return redirect('detailed_report', request.session['rep_key'])
    context = {'form':form, 'img':photo2.ph_link2}
    return render(request, 'reports/update-photo.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('detailed_report',pk = request.session['rep_key'])

def delete_photo2(request, pk):
    photo = Photo2.objects.get(id=pk)
    photo.delete()
    return redirect('detailed_report',pk = request.session['rep_key'])