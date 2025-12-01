
from django.shortcuts import render

def index(request):

	from .models import About, Service, Feature, Product, Team, Testimonial, Gallery
	about = About.objects.first()
	services = Service.objects.all()
	features = Feature.objects.all()
	products = Product.objects.order_by('-id')[:4]
	team = Team.objects.all()
	testimonials = Testimonial.objects.all()
	gallery = Gallery.objects.all()
	context = {
		'about': about,
		'services': services,
		'features': features,
		'products': products,
		'team': team,
		'testimonials': testimonials,
		'gallery': gallery,
	}
	return render(request, 'core/index.html', context)

def about(request):
	return render(request, 'core/about.html')

def contact(request):
	return render(request, 'core/contact.html')

def feature(request):
	return render(request, 'core/feature.html')

def gallery(request):
	return render(request, 'core/gallery.html')

def service(request):
	from .models import Service
	services = Service.objects.all()
	return render(request, 'core/service.html', {'services': services})

def team(request):
	from .models import Team
	team = Team.objects.all()
	return render(request, 'core/team.html', {'team': team})

def testimonial(request):
	from .models import Testimonial
	testimonials = Testimonial.objects.all()
	return render(request, 'core/testimonial.html', {'testimonials': testimonials})

def product(request):
	from .models import Product
	products = Product.objects.all()
	return render(request, 'core/product.html', {'products': products})

def notfound(request, exception=None):
	return render(request, '404.html', status=404)
