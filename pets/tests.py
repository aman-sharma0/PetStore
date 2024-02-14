from django.test import TestCase
from .models import Pet,Tag
print("--------")
class HomeUrlTests(TestCase):
    print("=======")
    def test_url(self):
       response= self.client.get("/")
       print(response)
       self.assertEqual(response.status_code,200)
# checj url existance: 
class ModelTests(TestCase):
    def test_tag_object(self):
        tag=Tag.objects.create(tagname="husky")
        self.assertEqual(tag.tagname,"husky1")
       
