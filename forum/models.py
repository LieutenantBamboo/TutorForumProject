from django.db import models
from django.template.defaultfilters import slugify


class Question(models.Model):
    max_length = 128
    title = models.CharField(max_length=max_length, unique=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    max_title_length = 128
    max_comment_length = 1024
    category = models.ForeignKey(Question)
    title = models.CharField(max_length=max_title_length)
    content = models.TextField(max_length=max_comment_length)
    views = models.IntegerField(default=0)
    pvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
