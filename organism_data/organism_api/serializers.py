from rest_framework import serializers
from .models import Taxonomy
from .models import Pfam
from .models import Protein
from .models import Domain

# creating the pfam serializer
class PfamSerializer(serializers.ModelSerializer):

    class Meta:
        # serializer uses the model Pfam to call the fields
        model = Pfam
        # serializer will return the respective fields in the api
        fields = ['domain_id', 'domain_description']

# creating the taxonomy serializer
class TaxonomySerializer(serializers.ModelSerializer):

    class Meta:
        # serializer uses the model Taxonomy to call the fields
        model = Taxonomy
        # serializer will return the respective fields in the api
        fields = ['taxa_id', 'clade', 'genus', 'species']

# creating the Domain serializer
class DomainSerializer(serializers.ModelSerializer):
    # calling the PfamSerializer to get the respective data for pfam_id
    pfam_id = PfamSerializer()

    class Meta:
        # serializer uses the model Domain to call the fields
        model = Domain
        # serializer will return the respective fields in the api
        fields = ['pfam_id', 'description', 'start', 'stop']

# creating the Protein serializer        
class ProteinSerializer(serializers.ModelSerializer):
    # calling the PfamSerializer and DomainSerializer to get the respective data for taxonomy and domains
    taxonomy = TaxonomySerializer()
    domains = DomainSerializer()

    class Meta:
        # serializer uses the model Protein to call the fields
        model = Protein
        # serializer will return the respective fields in the api
        fields = ['protein_id', 'sequence', 'taxonomy', 'length', 'domains']

# creating the Proteins serializer            
class ProteinsSerializer(serializers.ModelSerializer):

    class Meta:
        # serializer uses the model Protein to call the fields
        model = Protein
        # serializer will return the respective fields in the api
        fields = ['id','protein_id']

# creating the Pfams serializer    
class PfamsSerializer(serializers.ModelSerializer):
    # calling the PfamSerializer to get the respective data for pfam_id
    pfam_id = PfamSerializer(many=True)

    class Meta:
        # serializer uses the model Domain to call the fields
        model = Domain
        # serializer will return the respective fields in the api
        fields = ['id', 'pfam_id']

    # def create(self, validated_data):
    #     smth = self.initial_data.get('domain_id')
    #     new = Domain(**{**validated_data, 'domain_id': Pfam.objects.get(pk=smth['domain_id'])})

    #     new.save()
    #     return new

# class CoverageSerializer(serializers.ModelSerializer):
    
#     taxonomy = TaxonomySerializer()
#     domains = DomainSerializer()

#     for domains in Protein:
#         coverage =+ (Domain.start-Domain.stop)/Protein.length
    
#     class Meta:
#         model = Protein
#         fields = ['coverage']
        