from django.test import TestCase
from django.contrib.auth import get_user_model

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
        