from django.test import TestCase

# Create your tests here.

import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *

class Pfam_Test(APITestCase):

    def test_PfamReturnSuccess(self):
        pfam_factory = Pfam_Factory.create()
        url = reverse('Pfam', kwargs={'domain_id': 'PF01650'})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
    
    class Meta:
        model = Taxonomy




