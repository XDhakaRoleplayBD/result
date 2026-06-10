from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Result


def home(request):
    return render(request, 'home.html')


def result_page(request):
    results = Result.objects.all()
    return render(request, 'result.html', {'results': results})


def teacher_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            return redirect('teacher_dashboard')

    return render(request, 'teacher_login.html')


def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('student_dashboard')

    return render(request, 'student_login.html')


@login_required
def teacher_dashboard(request):
    results = Result.objects.all()
    return render(request, 'teacher_dashboard.html', {'results': results})


@login_required
def student_dashboard(request):
    results = Result.objects.all()
    return render(request, 'student_dashboard.html', {'results': results})


# UPLOAD RESULT
@login_required
def upload_result(request):
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES['image']

        Result.objects.create(
            title=title,
            image=image,
            uploaded_by=request.user
        )
        return redirect('teacher_dashboard')

    return render(request, 'upload_result.html')


# DELETE RESULT
@login_required
def delete_result(request, id):
    result = get_object_or_404(Result, id=id)
    result.delete()
    return redirect('teacher_dashboard')


def user_logout(request):
    logout(request)
    return redirect('home')