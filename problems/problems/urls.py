from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'problems.views.home', name='home'),
    # url(r'^problems/', include('problems.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'math_notepad.views.home'),
    url(r'^tag/(?P<tag_id>\d+)/$', 'math_notepad.views.tag'),
    url(r'^note/(?P<note_id>\d+)/$', 'math_notepad.views.note'),
    url(r'^admin/', include(admin.site.urls)),
)
