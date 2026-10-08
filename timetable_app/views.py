from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Timetable

# Create your views here.
def demo(request):
    return HttpResponse("this is my first django project")

def timetable_view(request):
    timetable = Timetable.objects.all()
    return render(request, 'timetable.html', {'timetable': timetable})
def add_timetable(request):
    if request.method == "POST":
        day = request.POST['day']
        subject = request.POST['subject']
        teacher = request.POST['teacher']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        Timetable.objects.create(
            day=day,
            subject=subject,
            teacher=teacher,
            start_time=start_time,
            end_time=end_time
        )

        return redirect('/timetable/')

    return render(request, 'add_timetable.html')
def edit_timetable(request, id):
    timetable = Timetable.objects.get(id=id)

    if request.method == "POST":
        timetable.day = request.POST['day']
        timetable.subject = request.POST['subject']
        timetable.teacher = request.POST['teacher']
        timetable.start_time = request.POST['start_time']
        timetable.end_time = request.POST['end_time']

        timetable.save()

        return redirect('/timetable/')

    return render(request, 'edit_timetable.html', {'timetable': timetable})
def delete_timetable(request, id):
    timetable = Timetable.objects.get(id=id)
    timetable.delete()
    return redirect('/timetable/')