from django.db import models


class Profile(models.Model):
    slug = models.SlugField(verbose_name="Slug профиля", null=True, blank=True, unique=True)
    name = models.CharField(verbose_name="Имя", max_length=25)
    description = models.CharField(verbose_name="Описание", max_length=120)
    avatar = models.ImageField(verbose_name="Изображение", upload_to="insta/upload/avatars/")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"({self.slug}) {self.name}"


class Post(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="Профиль", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(verbose_name="Картинка", upload_to="insta/upload/posts/")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.profile} - {self.id}"
