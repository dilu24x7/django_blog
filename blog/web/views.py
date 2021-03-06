import datetime

from web.models import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def home(request):
	entries = Entry.objects.order_by('created_on')
        return direct_to_template(request, 'web/home.html', {
		'entries': entries,
	})

def save_blog_details(request, entry):
	entry.title = request.POST['title']
	entry.content = request.POST['content']
	entry.created_by = request.user
	entry.created_on = datetime.datetime.now().date()
	entry.save()
	return HttpResponseRedirect(reverse('home'))

@login_required
def add_blog(request):
	if request.method == 'POST':
		entry = Entry()	
		entry.title = request.POST['title']
		entry.content = request.POST['content']
		entry.created_by = request.user
		entry.created_on = datetime.datetime.now().date()
		entry.save()
		return HttpResponseRedirect(reverse('home'))
	else:
		return direct_to_template(request, 'web/add_blog.html', {})

@login_required
def edit_blog(request, blog_id):
	entry = Entry.objects.get(id=blog_id)		
	if request.method == 'POST':
		entry.title = request.POST['title']
		entry.content = request.POST['content']
		entry.save()
		return HttpResponseRedirect(reverse('home'))
	else:
		return direct_to_template(request, 'web/edit_blog.html', {
			'entry': entry,
		})

@login_required
def delete_blog(request,blog_id):
	entry = Entry.objects.get(id=blog_id)	
	entry.delete()
	return HttpResponseRedirect(reverse('home'))

def login_view(request):
	if request.method == "GET":
		return direct_to_template(request, 'web/login.html', {})
	user = authenticate(username = request.POST['username'], password = request.POST['password'])
	if user is not None:
		login(request, user)
	else:
		return HttpResponse('Invalid login')
        return HttpResponseRedirect(reverse('home'))
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))

def detail(request, blog_id):
	entry = Entry.objects.get(id=blog_id)
	return direct_to_template(request, "web/details.html", { 'entry': entry })

