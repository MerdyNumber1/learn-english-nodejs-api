from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self) -> str:
        return str(self.title)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self) -> str:
        return str(self.title)
