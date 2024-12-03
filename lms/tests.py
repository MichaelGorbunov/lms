from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Lesson, Course, Subscription
from users.models import CustomUser

class SubscriptionTestCase(APITestCase):
    """тестирование подписки"""

    def setUp(self):
        self.user = CustomUser.objects.create(email='admin@example.com', is_staff=True, is_superuser=True)
        self.course = Course.objects.create(title='course_test', description='course_test', owner=self.user)
        self.lesson = Lesson.objects.create(title='lesson_test', description='lesson_test', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        """create"""
        url = reverse('lms:course-subscription')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'Подписка добавлена'}
        )

    def test_subscription_delete(self):
        """delete"""
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('lms:course-subscription')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'Подписка удалена'}
        )
