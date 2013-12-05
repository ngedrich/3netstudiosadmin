from django.shortcuts import render

from shows.models import Show, Category, Format, Photo

def index(request):
	show_list = Show.objects.all()
	return render(request, 'shows/index.html', {'show_list': show_list}, content_type = "application/json")