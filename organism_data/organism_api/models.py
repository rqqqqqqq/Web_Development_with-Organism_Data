from django.db import models 

# Creation of Taxonomy model
class Taxonomy(models.Model):
    taxa_id = models.CharField(max_length = 30, null = False, blank = False)
    clade = models.CharField(max_length = 1, default ='E')
    genus = models.CharField(max_length = 256, null = False, blank = False)
    species = models.CharField(max_length = 256, null = False, blank = False)
    def __str__(self):
        return str(self.taxa_id)

# Creating the Pfam model
class Pfam(models.Model):
    domain_id = models.CharField(max_length = 30, null = False, blank = False)
    domain_description = models.CharField(max_length = 256, null = False, blank = False)
    def __str__(self):
        return self.domain_id

# Creating the Domain model
class Domain(models.Model):
    # pfam_id is a foreign key
    pfam_id = models.ForeignKey(Pfam, on_delete = models.CASCADE)
    description = models.CharField(max_length = 256, null = False, blank = False)
    start = models.IntegerField(null = False, blank = False)
    stop = models.IntegerField(null = False, blank = False)

#Creating the Protein model
class Protein(models.Model):
    protein_id = models.CharField(max_length = 30, null = False, blank = False)
    sequence = models.CharField(max_length = 256, null = False, blank = False)
    # taxonomy is a foreign key
    taxonomy = models.ForeignKey(Taxonomy, on_delete = models.CASCADE)
    length = models.CharField(max_length = 8, null = False, blank = False)
    domains = models.ManyToManyField(Domain, through='Domain_protein_link')
    def __str__(self):
        return str(self.protein_id)    

# Creating the linker model to link between domain and protein models
class Domain_protein_link(models.Model):
    #domain and protein are foreign keys
    domain = models.ForeignKey(Domain, on_delete = models.CASCADE)
    protein = models.ForeignKey(Protein, on_delete = models.CASCADE)
    def special_save(self):
        pass    



