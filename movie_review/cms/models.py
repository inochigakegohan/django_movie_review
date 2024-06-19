from django.db import models


class Movie(models.Model):
    """映画"""
    name = models.CharField('映画名', max_length=255)
    publisher = models.CharField('配給会社', max_length=255, blank=True)
    page = models.IntegerField('上映時間', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Movie, verbose_name='映画名', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment
