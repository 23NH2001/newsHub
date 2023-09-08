from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class UserManagersTest(TestCase):
    global User 
    User = get_user_model()
    
    def test_create_user(self):
        # User = 
        user = User.objects.create_user(
            username = "test",
            email = "test@example.com",
            password = "TestPass123",
        )
        
        self.assertEqual(user.username,'test')
        self.assertEquals(user.email,"test@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username = "test",
            email = "test@example.com",
            password = "TestPass123",
        )
        self.assertEqual(admin_user.username,'test')
        self.assertEquals(admin_user.email,"test@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
class SignUpTests(TestCase):
    def response_get(self,query):
        return self.client.get(query)
    
    def test_url_exist_at_correct_location_signupview(self):
        response = self.response_get("/accounts/signup/")
        self.assertEqual(response.status_code,200)
    
    def test_signup_view_name(self):
        response = self.response_get(reverse("signupPage"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"registration/signupPage.html")
        
    def test_signup_form(self):
        response = self.client.post(reverse("signupPage"),
                                    {
                                        'first_name':'test',
                                        'last_name':'user',
                                        'username':'testuser',
                                        'email':'test1@example.com',
                                        'age':18,
                                        'password1':'@F6g**uJJZu&mU3',
                                        'password2':'@F6g**uJJZu&mU3',
                                     })
        self.assertEqual(response.status_code,302)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email,'test1@example.com')
        
        