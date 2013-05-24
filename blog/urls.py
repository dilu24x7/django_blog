from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.home', name='home'),
    url(r'^login/', 'web.views.login_view', name='login'),
    url(r'^logout/', 'web.views.logout_view', name='logout'),
    url(r'^add/entry/', 'web.views.add_blog', name='add_blog'),
    url(r'^edit/entry/(?P<blog_id>\d+)/', 'web.views.edit_blog', name='edit_blog'),
    url(r'^entry/(?P<blog_id>\d+)/', 'web.views.detail', name='entry'),
    url(r'^delete/entry/(?P<blog_id>\d+)/', 'web.views.delete_blog', name='delete_blog'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
