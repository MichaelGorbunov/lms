from django.db import models

from config import settings

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название курса", help_text="Course Title"
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Course Description", **NULLABLE
    )
    preview = models.ImageField(
        upload_to="lms/courses/",
        verbose_name="Превью курса",
        help_text="Course Preview",
        default="lms/courses/default.jpg",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="укажите владельца",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ["title"]


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="lessons",
    )
    title = models.CharField(
        max_length=150, verbose_name="Название урока", help_text="Lesson Title"
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Lesson Description"
    )
    preview = models.ImageField(
        upload_to="lms/lessons/",
        verbose_name="Превью урока",
        help_text="Lessons Preview",
        default="lms/lessons/default.jpg",
        **NULLABLE,
    )
    video_url = models.URLField(
        verbose_name="Ссылка на урок", help_text="Video URL", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="укажите владельца",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["title"]


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, verbose_name="Курс в подписке", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
