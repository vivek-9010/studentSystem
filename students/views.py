from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  # Added for search functionality
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator

def student_list(request):
    search_query = request.GET.get('q', '')
    
    if search_query:
        students = Student.objects.filter(
            Q(name__icontains=search_query) |
            Q(roll__icontains=search_query) |
            Q(branch__icontains=search_query)
        )
    else:
        students = Student.objects.all()
    
    # Add ordering to ensure consistent pagination
    students = students.order_by('-id')
    
    # Pagination
    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students/student_list.html', {
        'students': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'search_query': search_query  # Pass search query to template
    })

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            # Redirect to detail view after creation
            return redirect('student_detail', pk=student.pk)
        else:
            print(form.errors)  # Debug
    else:
        form = StudentForm()
    
    return render(request, 'students/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            # Redirect to detail view after update
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})
# students/views.py
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})