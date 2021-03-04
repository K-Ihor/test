from django.db import models
from django.urls import reverse


class News_post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    author = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    likes = models.IntegerField(default=0, verbose_name='Количество голосов')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Новостной пост'
        verbose_name_plural = 'Новостные посты'
        ordering = ['-created_at']


class Comment(models.Model):
    news = models.ForeignKey(News_post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.news)

    def get_absolute_url(self):
        return reverse('comment', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['created_at']