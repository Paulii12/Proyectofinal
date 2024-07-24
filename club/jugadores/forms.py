from socket import fromshare
from django import forms 
from .models import Jugador

class JugadorForm(forms.ModelForm):
    class Meta:
        model=Jugador
        #fields='__all__'
        fields=('id_jugador','DNI','','nom','fechan','altura',"peso","dire","cd","id_deporte","talla")
        labels ={
            "id_jugador" : "id del jugador" ,
            "DNI" : "DNI del jugador" ,
            'nom': 'nombre y apellido del jugador:',
            "fechan" : "fehca de nacimiento del jugador" ,
            "altura" : "altura del jugador" ,
            "peso" : "peso del jugador" , 
            "dire" : "direccion del jugador",
            "cd" : "codigo postal del jugador" ,
            "id_deporte" : "ID del deporte al que pertenece el jugador",
          #  "nummac" : "numero de macc " ,
            "talla" : "talla de indumentaria ",
                   
        
        }
        
    
    def __init__(self, *args, **kwargs):
        super(JugadorForm,self).__init__(*args,**kwargs)
        self.fields['lenguaje'].empty_label="Selecciona"
        self.fields['so'].empty_label="Selecciona"
        self.fields['ap'].required=True
        self.fields['am'].required=False
        