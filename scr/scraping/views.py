from django.shortcuts import render
from .models import Vacancy, Language
# Create your views here.
def home_view (request):
    qs = Vacancy.objects.all()
    lg = Language.objects.all()
    return render(request, 'home.html', {'object_list': qs},{'object_lis2': lg})