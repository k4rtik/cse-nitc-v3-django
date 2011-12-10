from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^csed/', include('csed.foo.urls')),

    (r'^news/$', 'csed.news.views.index'),
    (r'^news/(?P<newsitem_id>\d+)/$', 'csed.news.views.detail'),
    (r'^news/archive/$', 'csed.news.views.archive'),

    (r'^people/$', 'csed.people.views.index'),

    (r'^people/faculty/$', 'csed.people.views.faculty'),
    (r'^people/staff/$', 'csed.people.views.staff'),
    (r'^people/students/$', 'csed.people.views.students'),
    (r'^people/alumni/$', 'csed.people.views.alumni'),

    (r'^people/faculty/(?P<facultymember_id>\d+)/$', 'csed.people.views.facultymember_detail'),
    (r'^people/staff/(?P<staffmember_id>\d+)/$', 'csed.people.views.staffmember_detail'),
    (r'^people/students/(?P<student_id>\d+)/$', 'csed.people.views.student_detail'),
    (r'^people/alumni/(?P<alumnus_id>\d+)/$', 'csed.people.views.alumnus_detail'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

#    (r'^feedback/', 'csed.feedback.views.index'),
#    (r'^feedback/submit', 'csed.feedback.views.submit'),
#    (r'', 'csed.news.views.latest_5'),

)
