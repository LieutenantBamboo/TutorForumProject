from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name


class QuestionPage(models.Model):
    pass


class Question(models.Model):
    category = models.ForeignKey(Category)
    max_length = 128
    title = models.CharField(max_length=max_length, unique=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    text_field = models.CharField(max_length=10000, unique=False)
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


class UserProfile(models.Model):
    # Required Line - links class to model instance
    user = models.OneToOneField(User)

    # Additonal Attributes:
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # __unicode__() override
    def __str__(self):
        return self.user.username

    # Defined for compatability's sake
    def __unicode__(self):
        return self.user.username
