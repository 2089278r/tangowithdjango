from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    view = models.IntegerField(default = 0, unique=False)
    likes = models.IntegerField(default = 0, unique=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class PageAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'category', 'url')

    def __unicode__(self):
        return self.title