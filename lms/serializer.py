from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms.models import Course, Lesson, Subscription
from lms.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    # lesson_list = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(many=True, read_only=True, source="lessons")
    lesson_count = serializers.SerializerMethodField(read_only=True)

    subscription = SerializerMethodField()

    # def get_lessons_count(self, lesson):
    #     return Lesson.objects.filter(course=lesson).count()

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    # def get_lesson_list(self, obj):
    #     # Получение информации об уроках, связанных с данным курсом
    #     return LessonSerializer(obj.lessons.all(), many=True).data

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        # fields = "__all__"
        fields = (
            "pk",
            "title",
            "description",
            "lesson",
            "lesson_count",
            "owner",
            "preview",
            "subscription",
        )

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'