import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *

# creating dummy data for Taxonomy_Factory by using Taxonomy
class Taxonomy_Factory(factory.django.DjangoModelFactory):
    taxa_id = 53326
    clade = "E"
    genus = "Ancylostoma"
    species = "ceylanicum"
    
    class Meta:
        model = Taxonomy

# creating dummy data for Pfam_Factory by using Pfam
class Pfam_Factory(factory.django.DjangoModelFactory):
    domain_id = "PF01650"
    domain_description = "PeptidaseC13family"

    class Meta:
        model = Pfam

# creating dummy data for Domain_Factory by using Domain
class Domain_Factory(factory.django.DjangoModelFactory):
    pfam_id = factory.SubFactory(Pfam_Factory)
    description = "Peptidase C13 legumain"
    start = 40
    stop = 94

    class Meta:
        model = Domain

# creating dummy data for Protein_Factory by using Protein
class Protein_Factory(factory.django.DjangoModelFactory):
    protein_id = "A0A016S8J7"
    sequence = "MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA"
    taxonomy = factory.SubFactory(Taxonomy_Factory)
    length = 101
    domains = factory.SubFactory(Domain_Factory)

    class Meta:
        model = Protein

# creating dummy data for Domain_protein_link_Factory by using Domain_protein_link
class Domain_protein_link_Factory(factory.django.DjangoModelFactory):
    domain = factory.SubFactory(Domain_Factory)
    protein = factory.SubFactory(Protein_Factory)

    class Meta:
        model = Domain_protein_link
