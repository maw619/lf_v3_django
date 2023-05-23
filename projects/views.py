from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.models import Project
from .forms import ProjectForm



@login_required(login_url='/login/')
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects, 'tabletitle': 'Projects'.upper()}
    return render(request, 'projects/projects.html', context)

@login_required(login_url='/login/')
def add_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/add-project.html', {'form':form})

@login_required(login_url='/login/')
def update_project(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/update-project.html', {'form':form})

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('projects')