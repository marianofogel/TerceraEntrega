from django.contrib import admin
from .models import * #importamos el archivo models

# Register your models here.#registramos los modelos

admin.site.register(Futbol)
admin.site.register(Voley)
admin.site.register(Handball)
admin.site.register(Tenis)
admin.site.register(Deportista)
