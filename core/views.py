
from django.shortcuts import render

def index(request):
	return render(request, 'core/index.html')

def about(request):
	return render(request, 'core/about.html')

def contact(request):
	return render(request, 'core/contact.html')

def feature(request):
	return render(request, 'core/feature.html')

def gallery(request):
	return render(request, 'core/gallery.html')

def service(request):
	return render(request, 'core/service.html')

def team(request):
	return render(request, 'core/team.html')

def testimonial(request):
	return render(request, 'core/testimonial.html')

def product(request):
	return render(request, 'core/product.html')

def notfound(request, exception=None):
	return render(request, '404.html', status=404)
