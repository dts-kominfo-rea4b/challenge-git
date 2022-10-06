from django.db import models


# Create your models here.
class StudentMember(models.Model):
    """Anggota perpustakaan, siswa"""
    nis = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    status = models.CharField(max_length=20)
    first_fmd = models.BinaryField(max_length=4000)
    second_fmd = models.BinaryField(max_length=4000)
