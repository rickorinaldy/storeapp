import pandas as pd
from .models import *

def simpan():
    data = pd.read_excel('data\data barang.xlsx')
    print('Menyimpan data..')
    for i in range(len(data)):
        try:
            try:
                BarangModel.objects.filter(no_id=i).update(
                    nama            = data['Barang'][i],
                    harga           = data['Harga'][i],
                    harga_renceng   = data['Harga Rencengan'][i])
            except:
                BarangModel(
                    no_id           = i,
                    nama            = data['Barang'][i],
                    harga           = data['Harga'][i],
                    harga_renceng   = data['Harga Rencengan'][i],
                ).save()
        except Exception as e:print(e)

    print('Berhasil disimpan')
