import os
import sys
import django
import csv
from collections import defaultdict

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
sys.path.append(PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'organism_data.settings')
django.setup()
from organism_api.models import Domain, Taxonomy, Pfam, Protein, Domain_protein_link

# naming the csv files
data_seq_file = 'data/assignment_data_sequences.csv'
data_set_file = 'data/assignment_data_set.csv' 
pfam_data_file = 'data/pfam_descriptions.csv'


# creating empty sets to put values in later
pfam = set()
taxonomy = set()
domain = set()
protein = set()
domain_protein_link = set()
test = set()
testing = set()

# opening the assignment_data_sequences csv file
with open(data_seq_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        # saving elements 0 and 1 in csv file into temporary set named testing
        testing.add((row[0], row[1]))

# opening the pfam_descriptions csv file
with open(pfam_data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        # saving elements 0 and 1 in csv file into temporary set named test
        test.add((row[0], row[1]))

# opening the assignment_data_set csv file
with open(data_set_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        # splitting genus species pairs by spacing
        genusSpecies_pairs = row[3].split(" ")

        for var in range(len(genusSpecies_pairs)):
            if (var>1):
                # saving element in index 1, 2, 3, and so on into genusSpecies_pairs[1]
                genusSpecies_pairs[1] += genusSpecies_pairs[var]

        # for each entry in the test set and for each row in the csv_reader, 
        # add each specific element into the relevant temporary sets
        for entry in test:
            pfam.add((row[5], row[4]))
            taxonomy.add((row[1], row[2], genusSpecies_pairs[0], genusSpecies_pairs[1]))
            domain_protein_link.add((row[5], row[0]))

            # ensure there is no duplicate data
            if entry[0] == row[5]:
                domain.add((entry[0], entry[1], row[6], row[7]))

        # for each entry_ in the testing set and for each row in the csv_reader, 
        # add each specific element into the relevant temporary sets
        for entry_ in testing:
            # ensure there is no duplicate data
            if entry_[0] == row[0]:
                protein.add((entry_[0], row[1], row[8], row[5], entry_[1]))

# temporary storage for all tables that have fk linked to ur table
pfam_rows = {}
taxonomy_rows = {}
domain_rows = {}
protein_rows = {}

#remove everything from database and repopulate again
Pfam.objects.all().delete()
Taxonomy.objects.all().delete()
Protein.objects.all().delete()
Domain_protein_link.objects.all().delete()
Domain.objects.all().delete()


# saving the relevant elements into the Pfam table in order
for pfam_entry in pfam:
    row = Pfam.objects.create(domain_id = pfam_entry[0], domain_description = pfam_entry[1])
    row.save()
    pfam_rows[pfam_entry[0]] = row

# saving the relevant elements into the Taxonomy table in order
for taxonomy_entry in taxonomy:
    row = Taxonomy.objects.create(taxa_id = taxonomy_entry[0], 
                                clade = taxonomy_entry[1],
                                genus = taxonomy_entry[2],
                                species = taxonomy_entry[3])
    row.save()
    # saving data into taxonomy_rows to be called as a foreign key in another table later
    taxonomy_rows[taxonomy_entry] = row

# saving the relevant elements into the Domain table in order
for domain_entry in domain:
    row = Domain.objects.create(
                                pfam_id = pfam_rows[domain_entry[0]], 
                                description = domain_entry[1],
                                start = domain_entry[2],
                                stop = domain_entry[3])
    row.save()
    domain_rows[domain_entry] = row

# saving the relevant elements into the Protein table in order
for protein_entry in protein:
    row = Protein.objects.create(protein_id = protein_entry[0], 
                                sequence = protein_entry[4],
                                taxonomy = taxonomy_rows[taxonomy_entry],
                                length = protein_entry[2])
    # to populate the linker table
    row.domains.add(domain_rows[domain_entry])
    row.save()
    protein_rows[protein_entry] = row


    # for protein_entry in protein:
    # if(Protein.objects.filter(pk=protein.id).exists()):
    #     sequence = protein_entry[4],
    #     taxonomy = taxonomy_rows[taxonomy_rows[protein_entry[1]]],
    #     length = protein_entry[2])
    
    # else:  
    #     row = Protein.objects.create(protein_id = protein_entry[0], 
    #                                 sequence = protein_entry[4],
    #                                 taxonomy = taxonomy_rows[taxonomy_rows[protein_entry[1]]],
    #                                 length = protein_entry[2])
    # # to populate the linker table
    # row.domains.add(domain_rows[domain_entry])
    # row.save()
    # protein_rows[protein_entry] = row
