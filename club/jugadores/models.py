from typing import Any
from django.db import models

class Deporte():
    id_deporte=models.AutoField(primary_key=True,verbose_name="Deporte")
    descripcion=models.CharField(max_length=50,verbose_name="Nombre Deporte")
    
    def __str__(self):
        fila=self.id_deporte+self.descripcion
    
# Create your models here.
class Jugador(models.Model):
    id_jugador=models.AutoField(primary_key=True)
    DNI=models.BigIntegerField(max_length=8,verbose_name="DNI")
    nom = models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fechan=models.DateField(verbose_name="Fecha Nacimiento")
    altura=models.AutoField(max_length=3,verbose_name="Altura")
    peso=models.AutoField(max_length=3,verbose_name="Peso")
    dire=models.DateField(max_length=50,verbose_name="Direccion")
    cd=models.DateField(max_length=6,verbose_name="codigo postal")
   # nummac=models(max_length=6,verbose_name="numero de mac")
    talla=models.CharField(max_length=6,verbose_name="numero de talla indumentaria")
    id_deporte=models.ForeignKey("app.Model", verbose_name=("Deporte"), on_delete=models.CASCADE)
    
    
    def __str__(self):
        fila="id_jugador"+str(self.id_jugador)+ "-" + "nom: " + self.nom
        return fila
    
    #def delete(self, using=None, keep_parents=False):
      #  self.foto.storage.delate(self.foto.name)
      #  return super().delet