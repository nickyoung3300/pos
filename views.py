from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Menu

def postest1(request):
	posMenu = Menu.objects.select_related('category').all()

	
	context = {
		"Menu":posMenu
	}

	
	return render(request, "pos/posbase.html", context=context)

# Create your views here.
