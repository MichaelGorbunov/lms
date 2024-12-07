from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import CustomUser


class SubscriptionTestCase(APITestCase):
    """тестирование подписки"""

    def setUp(self):
        self.user = CustomUser.objects.create(
            email="admin@example.com", is_staff=True, is_superuser=True
        )
        self.course = Course.objects.create(
            title="course_test", description="course_test", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="lesson_test",
            description="lesson_test",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        """create"""
        url = reverse("lms:course-subscription")
        data = {"user": self.user, "course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "Подписка добавлена"})

    def test_subscription_delete(self):
        """delete"""
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        url = reverse("lms:course-subscription")
        data = {"user": self.user, "course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "Подписка удалена"})


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            email="admin@example.com", is_staff=True, is_superuser=True
        )
        self.course = Course.objects.create(
            title="course_test", description="course_test", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="lesson_test",
            description="lesson_test",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse("lms:lesson-create")
        data = {"title": "lesson_test", "description": "lesson_test"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson-get", args=(self.lesson.pk,))
        response = self.client.get(url)
        print(response.json())
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_update(self):
        url = reverse("lms:lesson-update", args=(self.lesson.pk,))
        data = {"title": "Python"}
        response = self.client.patch(url, data)
        print((response.json()))
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Python")

    def test_lesson_delete(self):
        url = reverse("lms:lesson-delete", args=(self.lesson.pk,))

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lesson-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email="admin@example.com")
        self.course = Course.objects.create(
            title="course_test", description="course_test", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="lesson_test",
            description="lesson_test",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = f"/lms/course/{self.course.pk}/"
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_course_create(self):
        url = "/lms/course/"
        data = {"title": "course_test", "description": "course_test"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        url = f"/lms/course/{self.course.pk}/"
        data = {"title": "Python"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Python")

    def test_course_delete(self):
        url = f"/lms/course/{self.course.pk}/"

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        url = "/lms/course/"
        response = self.client.get(url)

        data = response.json()
        print(data)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": self.course.pk,
                    "title": self.course.title,
                    "description": self.course.description,
                    "lesson": [
                        {
                            "id": self.lesson.pk,
                            "title": self.lesson.title,
                            "description": self.lesson.description,
                            "preview": "http://testserver/media/lms/lessons/default.jpg",
                            "video_url": None,
                            "course": self.course.pk,
                            "owner": self.user.pk,
                        }
                    ],
                    "lesson_count": self.course.lessons.count(),
                    "owner": self.user.pk,
                    "preview": "http://testserver/media/lms/courses/default.jpg",
                    "subscription": False,
                }
            ],
        }
        print(result)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


# coverage run --source='.' manage.py test
# coverage report
