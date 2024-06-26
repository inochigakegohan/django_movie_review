from django.db import models


class Movie(models.Model):
    """作品"""
    name = models.CharField('作品名', max_length=255)
    company = models.CharField('配給会社', max_length=255, blank=True)
    time = models.IntegerField('上映時間', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    movie = models.ForeignKey(Movie, verbose_name='作品', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

