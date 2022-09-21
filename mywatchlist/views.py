from django.shortcuts import render
from mywatchlist.models import BarangMyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):
    data_barang_watchlist = BarangMyWatchlist.objects.all()
    context = {
    'film': data_barang_watchlist,
    'nama': 'Zacky Muchlas Dharmawan',
    'npm' : '2106702296'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangMyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = BarangMyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = BarangMyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
