from django.contrib import admin
from django.urls import path
#from . import favoritos
from app.views import favoritos

urlpatterns = [
    path('', favoritos.index_page, name='index-page'),
    path('login/', favoritos.index_page, name='login'),
    path('home/', favoritos.home, name='home'),
    path('buscar/', favoritos.search, name='buscar'),

    path('favourites/', favoritos.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', favoritos.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', favoritos.deleteFavourite, name='borrar-favorito'),

    path('exit/', favoritos.exit, name='exit'),
]