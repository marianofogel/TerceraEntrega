from django.urls import path
from AppTerceraEntrega import views

urlpatterns = [
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    path('futbol', views.futbol, name="futbol"),
    path('voley', views.voley, name="voley"),
    path('handball', views.handball, name="handball"),
    path('tenis', views.tenis, name="tenis"),
    path('deportistasFormulario', views.deportistasFormulario, name="deportistasFormulario"),
    path('buscarDeporte', views.buscarDeporte, name='BuscarDeporte'),
    path('busqueda', views.busqueda)

]