from django.db import models

PROGRAM_CHOICES = (
	('B', 'BTech'),
	('M', 'MTech CSE'),
	('S', 'MTech CSE (IS)'),
	('C', 'MCA'),
	('P', 'PhD'),
)

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female')
)

class Person(models.Model):
	first_name = models.CharField("First Name", max_length=50)
	last_name = models.CharField("Last Name", max_length=50, blank=True)
	email = models.EmailField("Email ID", max_length=75, blank=True)#, unique=True)

	class Meta:
		abstract = True

class FacultyMember(Person):
	def __unicode__(self):
		return self.title + ' ' + self.first_name + ' ' + self.last_name
	#__unicode__.admin_order_field = 'first_name'
	class Meta:
		verbose_name_plural = "Faculty"
	title = models.CharField("Title", max_length=2, blank=True)
	position = models.CharField("Position", max_length=30)
	status = models.CharField(max_length=100, blank=True, help_text="Whether on leave and reason for that.")
	qualification = models.CharField(max_length=100, blank = True)
	research_interests = models.TextField("Areas of Interest")
	phone = models.CharField("Phone Number", max_length=20, blank=True)
	photo = models.ImageField(upload_to = 'photos/faculty', blank = True)
	homepage = models.URLField(blank = True)

class StaffMember(Person):
	def __unicode__(self):
		return self.first_name + ' ' + self.last_name
	class Meta:
		verbose_name_plural = "Staff"
	position = models.CharField("Position", max_length=30)
	phone = models.CharField("Phone Number", max_length=20, blank=True)
	photo = models.ImageField(upload_to = 'photos/staff', blank = True)
	homepage = models.URLField(blank = True)

class Student(Person):
	def __unicode__(self):
		return self.first_name + ' ' + self.last_name
	def year_of_admission(self):
		yoa = self.rollno[1:3]
		if yoa[0] == 'S':
			y = "2004"
			yoa = y[2:]
		elif yoa[0] == '2':
			y = "2002"
			yoa = y[2:]
		elif yoa[0] == '3':
			y = "2003"
			yoa = y[2:]
		yoa = '20' + yoa
		return yoa
	year_of_admission.admin_order_field = 'rollno'
	rollno = models.CharField("Roll Number", max_length=9)
	program = models.CharField(max_length=1, choices=PROGRAM_CHOICES)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	homepage = models.URLField(blank = True)

class Alumnus(Person):
	def __unicode__(self):
		return self.first_name + ' ' + self.last_name
	class Meta:
		verbose_name_plural = "Alumni"
	program = models.CharField(max_length=1, choices=PROGRAM_CHOICES)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	year_of_admission = models.CharField(max_length=4)
	homepage = models.URLField(blank = True)

