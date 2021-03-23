from django.shortcuts import render
from .models import Vacancy, Language
# Create your views here.
def home_view (request):
    qs = Vacancy.objects.all()
    lg = Language.objects.all()

    return render(request, 'scraping/home.html', {'object_list': qs})

