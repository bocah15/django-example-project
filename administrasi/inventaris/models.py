from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Inventaris(models.Model):
  KONDISI_BARANG = (
    ('baik', 'Baik'),
    ('sedang', 'Sedang'),
    ('rusak', 'Rusak'),
  )
  nomor             = models.CharField(max_length=255, blank=False, null=False, unique=True,
                      error_messages={
                          'unique': _(
                              "Nomor Inventaris Sudah ada"),
                      })
  nama_barang       = models.CharField(max_length=255)
  jumlah            = models.IntegerField(default=1)
  kondisi_barang    = models.CharField(max_length=20, choices=KONDISI_BARANG, default='baik')