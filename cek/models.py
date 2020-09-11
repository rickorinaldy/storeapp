from django.db import models

# Create your models here.
class BarangModel(models.Model):
    nama            = models.CharField(primary_key=True, max_length=160)
    harga           = models.IntegerField(blank=True, null=True)
    harga_renceng   = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.nama} - {self.harga}"
