from django.db import models

# Create your models here.

class Doone(models.Model):
    id = models.IntegerField(primary_key=True)
    nomcapteur = models.CharField(max_length=100)
    piece = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.id} {self.nomcapteur} {self.piece} {self.emplacement}"
        return chaine
    def Doe(self):
        return{"id":self.id, "nomcapteur":self.nomcapteur, "piece":self.piece, "emplacement":self.emplacement}


class stamp(models.Model):
    idd = models.ForeignKey(Doone, on_delete=models.CASCADE)
    t1 = models.DateTimeField()

    def __str__(self):
        chaine2 =f"{self.idd} {self.t1}"
        return chaine2

    def eod(self):
        return{"id":self.idd, "température":self.t1}
