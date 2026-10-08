from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student
@login_required
def home(request):
    return render(request, 'students/home.html')
@login_required
def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'students/add_student.html', {'form': form})
@login_required
def view_students(request):
    students = Student.objects.all()
    return render(request, 'students/view_students.html', {'students': students})

@login_required
def edit_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('/students/')

    return render(request, 'students/edit_student.html', {'form': form})
@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students/')
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')

    return render(request, 'students/login.html')
def user_logout(request):
    logout(request)
    return redirect('/login/')