from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTest(SimpleTestCase):
    def response_get(self,query):
        return self.client.get(query)
    
    def test_url_exist_at_correct_location(self):
        res = self.response_get("/")
        self.assertEqual(res.status_code,200) # hompage can be access using it's URL name
    
    def test_homepage_view(self):
        res = self.client.get(reverse("homePage"))
        self.assertEqual(res.status_code,200) # hompage can be access using it's URL name
        self.assertTemplateUsed(res,'homePage.html') # homePage is using the given template name
        self.assertContains(res,"Home") # homePage containe 'Home'
        