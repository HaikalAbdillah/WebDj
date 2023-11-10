from django.db import models

# Create your models here.

class Menu(models.Model):
  nama = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.nama}"
  
class Blog(models.Model):
  menu = models.ForeignKey(Menu, on_delete=models.Case)
  namaProduk = models.CharField(max_length=100)
  harga = models.IntegerField()

  def __str__(self):
    return f"{self.namaProduk} {self.harga}"
