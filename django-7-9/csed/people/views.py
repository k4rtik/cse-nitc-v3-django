from django.shortcuts import render_to_response, get_object_or_404
from csed.people.models import FacultyMember, StaffMember, Student, Alumnus
from django.http import HttpResponse

def index(request):
    people_list = ['Faculty', 'Staff', 'Students', 'Alumni']
    return render_to_response('people/index.html', {'people_list': people_list})

def faculty(request):
    return HttpResponse("You are at the faculty page")

def staff(request):
    return HttpResponse("You are at the staff page")

def students(request):
    return HttpResponse("You are at the students page")

def alumni(request):
    return HttpResponse("You are at the alumni page")

def facultymember_detail(request, facultymember_id):
    return HttpResponse("You are at the faculty member " + facultymember_id + " detail")

def staffmember_detail(request, staffmember_id):
    return HttpResponse("You are at the staff member " + staffmember_id + " detail")

def student_detail(request, student_id):
    return HttpResponse("You are at the student " + student_id + " detail")

def alumnus_detail(request, alumnus_id):
    return HttpResponse("You are at the alumnus " + alumnus_id + " detail")
