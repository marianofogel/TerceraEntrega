from django import forms

class DeportistasFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    altura = forms.CharField()
    deporte = forms.CharField(max_length=20)
    contacto = forms.IntegerField()
    
class Futbolistas(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    posicion = forms.CharField(max_length=20)
    contacto = forms.IntegerField()

class Voleybolistas(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    altura = forms.FloatField()
    contacto = forms.IntegerField()

class Handballistas(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    altura = forms.FloatField()
    contacto = forms.IntegerField()

class Tenistas(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    mano_habil = forms.CharField(max_length=10)
    contacto = forms.IntegerField()