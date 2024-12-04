from rest_framework.test import APITestCase
from rest_framework import status
from teamapp.models import Member

class MemberViewTests(APITestCase):

    def setUp(self):
        self.member = Member.objects.create(first="Tom", last="Zurkan", email="tzurkan@gmail.com", phone="415-302-5571")

    def test_get_member_list(self):
        url = '/members/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_member_detail(self):
        url = f'/members/{self.member.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first'], "Tom")

    def test_create_member(self):
        url = '/members/'
        data = {'first':"Fred", 'last':"Stick", 'email':"stick@gmail.com", 'phone':"415-302-5555"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 2)

    def test_update_member(self):
        url = f'/members/{self.member.id}/'
        response = self.client.get(url)
        data = response.data
        data['first'] = "Ted"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first'], "Ted")

    def test_delete_member(self):
        url = f'/members/{self.member.id}/'
        response = self.client.delete(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
