from django.shortcuts import render

# TODO: Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Zacky Muchlas Dharmawan',
        'npm' : '2106702296'
        
    }
    return render(request, "katalog.html", context)
