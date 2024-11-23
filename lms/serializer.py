from rest_framework import serializers
from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson_list = serializers.SerializerMethodField(read_only=True)

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_lesson_list(self, obj):
        # Получение информации об уроках, связанных с данным курсом
        return LessonSerializer(obj.lessons.all(), many=True).data

    class Meta:
        model = Course
        fields = "__all__"
