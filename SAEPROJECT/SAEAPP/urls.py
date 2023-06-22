from django.urls import path
from . import views, viewsdeux


urlpatterns = [

    #path('index/', views.index),
    path('', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
    #
    path('appindex/', viewsdeux.appindex),
    path('appajout/', viewsdeux.appajout),
    path('apptraitement/', viewsdeux.apptraitement),
    path('appaffiche/<int:id>/', viewsdeux.appaffiche),
    path('appupdate/<int:id>/', viewsdeux.appupdate),
    path('appupdatetraitement/<int:id>/', viewsdeux.appupdatetraitement),
    path('appdelete/<int:id>/', viewsdeux.appdelete),

]