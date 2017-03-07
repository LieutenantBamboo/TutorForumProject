from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# College level (Only several Colleges)
class College(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# School Level (Many schools per College)
class School(models.Model):
    college = models.ForeignKey(College)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Module Level (Many modules per school)
class Module(models.Model):
    school = models.ForeignKey(School)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Master container of all post data per page
class QuestionPage(models.Model):
    module = models.ForeignKey(Module, null=True)
    max_length = 128
    title = models.CharField(max_length=max_length, unique=True, null=True)
    locked = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.title)
        super(QuestionPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


# Contains each question, whether it be a
class QuestionPost(models.Model):
    page = models.ForeignKey(QuestionPage)
    max_length = 128
    # Boolean as to wh
    question = models.BooleanField(default=False)
    title = models.CharField(max_length=max_length, unique=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    text_field = models.CharField(max_length=10000, unique=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


# Multiple comments may be posted per QuestionPost (Many to one relationship)
class Comment(models.Model):
    max_title_length = 128
    max_comment_length = 1024
    category = models.ForeignKey(QuestionPost)
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

    # Additional Attributes:
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # __unicode__() override
    def __str__(self):
        return self.user.username

    # Defined for the sake of compatibility
    def __unicode__(self):
        return self.user.username
