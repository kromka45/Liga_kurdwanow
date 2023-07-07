from django.db import models

# Create your models here.
class Zespol(models.Model):
    nazwa=models.CharField(max_length=25)
    l_meczy=models.IntegerField(default=0)
    punkty=models.IntegerField(default=0)
    zwyciestwa = models.IntegerField(default=0)
    remisy = models.IntegerField(default=0)
    porazki = models.IntegerField(default=0)
    b_zdobyte =models.IntegerField(default=0)
    b_stracone = models.IntegerField(default=0)
    bilans = models.IntegerField(default=0)





    def __str__(self):
        return self.nazwa






