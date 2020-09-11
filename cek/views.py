from django.shortcuts import render
from .models import BarangModel as bm
from .get_data import simpan

def show_data(request):
    simpan()
    return render(request, 'show.html', {'barang':bm.objects.all()})
