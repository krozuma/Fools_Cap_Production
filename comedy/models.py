from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    pic = models.ImageField(upload_to = 'images', blank=True)
    rank = models.IntegerField(default=0)
    cite = models.CharField(max_length=200, blank=True)
    alt = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, max_length = 250, null = True, blank = True)
    News = 'NE'
    Politics= 'PO'
    Sports = 'SP'
    Local = 'LO'
    Opinion = 'OP'
    Health = 'HE'
    Entertainment = 'EN'
    art_cats = (
        (News, 'News'),
        (Politics, 'Politics'),
        (Sports, 'Sports'),
        (Local, 'Local'),
        (Opinion, 'Opinion'),
        (Health, 'Health'),
        (Entertainment, 'Entertainment')
    )
    art_cat = models.CharField(max_length=2, choices=art_cats, default=News)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug, 'id':self.id})
