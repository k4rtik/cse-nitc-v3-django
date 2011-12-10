from csed.people.models import Person, FacultyMember, StaffMember, Student, Alumnus
from django.contrib import admin

class FacultyMemberAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name and Photo', {'fields':['title', 'first_name', 'last_name', 'photo']}),
		('Details', {'fields':['position', 'qualification', 'research_interests']}),
		('Contact Details', {'fields':['phone', 'email', 'homepage']}),
	]
	list_display = ('__unicode__', 'position', 'email')
	list_filter = ['position']
	search_fields = ['first_name', 'last_name']
	actions_on_top = False
	actions_on_bottom = True
admin.site.register(FacultyMember, FacultyMemberAdmin)

class StaffMemberAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name and Photo', {'fields':['first_name', 'last_name', 'photo']}),
		('Details', {'fields':['position']}),
		('Contact Details', {'fields':['phone', 'email', 'homepage']}),
	]
	list_display = ('__unicode__', 'position', 'email')
	list_filter = ['position']
	search_fields = ['first_name', 'last_name']
	actions_on_top = False
	actions_on_bottom = True
admin.site.register(StaffMember, StaffMemberAdmin)

class StudentAdmin(admin.ModelAdmin):
	fieldsets = [
		('Personal Details', {'fields':['first_name', 'last_name', 'gender']}),
		('Academic Details', {'fields':['program', 'rollno']}),
		('Contact Details', {'fields':['email', 'homepage']}),
	]
	list_display = ('__unicode__', 'gender', 'program', 'rollno', 'year_of_admission')
	list_filter = ['program', 'gender',]# 'year_of_admission']
	search_fields = ['first_name', 'last_name']
	actions_on_top = False
	actions_on_bottom = True
admin.site.register(Student, StudentAdmin)


class AlumnusAdmin(admin.ModelAdmin):
	fieldsets = [
		('Personal Details', {'fields':['first_name', 'last_name', 'gender']}),
		('Academic Details', {'fields':['program', 'year_of_admission']}),
		('Contact Details', {'fields':['email', 'homepage']}),
	]
	list_display = ('__unicode__', 'gender', 'program', 'year_of_admission')
	list_filter = ['program', 'year_of_admission', 'gender']
	search_fields = ['first_name', 'last_name']
	actions_on_top = False
	actions_on_bottom = True
admin.site.register(Alumnus, AlumnusAdmin)
