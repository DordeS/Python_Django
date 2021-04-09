from django.shortcuts import render
from stl_view.models import Stl_view

# Create your views here.
def stl_view(request, pk):
  stl_view = Stl_view.objects.get(pk=pk)
  context = {
    'stl_view': stl_view
  }
  return render(request, 'stl_view.html', context)

def home_page(request):
  return render(request, 'home_page.html')