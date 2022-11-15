from django.urls import reverse
from rest_framework.test import APITestCase

class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse('user_view')
        user_data = {
            "username":"tester",
            "password":"testpassword",
            "email":"test@test.com",
            "fullname":"테스터",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data["message"], "가입 완료!!")