from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = "api-overview"),

    path('protein/', views.Protein_add, name="Protein"), 
    path('protein/<str:protein_id>/', views.Protein_views, name="Protein"), 

    path('pfam/', views.Pfam_view, name="Pfam"), 
    path('pfam/<str:domain_id>/', views.Pfam_views, name="Pfam"), 
    
    path('proteins/', views.Proteins_view, name="Proteins"), 
    path('proteins/<str:taxa_id>/', views.Proteins_views, name="Proteins"), 

    path('pfams/', views.Pfams_view, name="Pfams"), 
    path('pfams/<str:taxa_id>/', views.Pfams_views, name="Pfams"), 
    
    # path('coverage/', views.Coverage_view, name="Coverage"), 
    # path('coverage/<str:protein_id>/', views.Coverage_view, name="Coverage"), 

] 