from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PfamSerializer
from .serializers import ProteinSerializer
from .serializers import ProteinsSerializer
from .serializers import PfamsSerializer
# from .serializers import CoverageSerializer

from .models import Pfam
from .models import Taxonomy
from .models import Protein
from .models import Domain
# Create your views here.

@api_view(['GET'])
def apiOverview(request): 
    api_urls = {
        'Protein': 'protein/',
        'Pfam': 'pfam/',
        'Proteins': 'proteins/',                
        'Pfams': 'pfams/',
        'Coverage': 'coverage/'
        }
    return Response(api_urls)

# creates the api to allow post, which is to add a new record
@api_view(['POST'])
def Protein_add(request):
    # allows new records to be added to ProteinSerializer
    serializer = ProteinSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# creates the api to return the given protein seq
@api_view(['GET'])
def Protein_views(request, protein_id):
    # get protein_id as user input in the url which corresponds to Protein table
    protein = Protein.objects.get(protein_id=protein_id)
    # check ProteinSerializer with the protein_id input
    serializer = ProteinSerializer(protein, many=True)
    return Response(serializer.data)
# error cos get returned more than 1 protein    

# not necessary, to show all objects in Pfam table that corresponds to PfamSerializer
@api_view(['GET'])
def Pfam_view(request):
    pfam = Pfam.objects.all()
    serializer = PfamSerializer(pfam, many=True)
    return Response(serializer.data)

# creates the api to return the domain and desc
@api_view(['GET'])
def Pfam_views(request,domain_id):
    # get domain_id as user input in the url which corresponds to Pfam table
    pfam = Pfam.objects.get(domain_id=domain_id)
    # check PfamSerializer with the domain_id input
    serializer = PfamSerializer(pfam, many=False)
    return Response(serializer.data)
#works

# not necessary, shows all protein objects for organisms
@api_view(['GET'])
def Proteins_view(request):
    protein = Protein.objects.all()
    serializer = ProteinsSerializer(protein, many=True)
    return Response(serializer.data)
# works 

# creates the api to return all proteins for given organism
@api_view(['GET'])
def Proteins_views(request, taxa_id):
    # get taxa_id as user input in the url which corresponds to Protein table
    taxa_ids  = Taxonomy.objects.get(taxa_id= taxa_id)
    protein = Protein.objects.filter(taxonomy=taxa_ids)
    # check ProteinsSerializer with the taxa_id input
    serializer = ProteinsSerializer(protein, many=True)
    return Response(serializer.data)
# does not work

# not necessary, shows all domain objects for organisms
@api_view(['GET'])
def Pfams_view(request):
    domain = Domain.objects.all()
    serializer = PfamsSerializer(domain, many=True)
    return Response(serializer.data)
# object not iterable

# creates the api to return all domains for given organism
@api_view(['GET'])
def Pfams_views(request, taxa_id):
    # get taxa_id as user input in the url which corresponds to Domain table
    domain = Domain.objects.get(taxa_id=taxa_id)
    # check PfamsSerializer with the taxa_id input
    serializer = PfamsSerializer(domain, many=False)
    return Response(serializer.data)




# @api_view(['GET'])
# def Coverage_view(request):
#     protein = Protein.objects.all()
#     serializer = CoverageSerializer(protein, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def Coverage_view(request, protein_id):
#     protein = Protein.objects.get(protein_id=protein_id)
#     serializer = CoverageSerializer(protein, many=False)
#     return Response(serializer.data)




