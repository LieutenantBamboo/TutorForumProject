from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# College level (Only several Colleges)
class College(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(College, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Colleges"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# School Level (Many schools per College)
class School(models.Model):
    college = models.ForeignKey(College)
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(School, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Module Level (Many modules per school)
class Module(models.Model):
    school = models.ForeignKey(School)
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Module, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Master container of all post data per page
class QuestionPage(models.Model):
    module = models.ForeignKey(Module, null=True)
    max_length = 128
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=max_length, unique=True, default='untitled')
    locked = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name_plural = "QuestionPages"

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.title)
        super(QuestionPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


# Contains each question, whether it be a question or an answer
class QuestionPost(models.Model):
    page = models.ForeignKey(QuestionPage)
    max_length = 128
    # Boolean as to whether it is a student question or a tutor answer
    question = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    text_field = models.CharField(max_length=10000, unique=False)

    class Meta:
        verbose_name_plural = "QuestionPosts"

    def __str__(self):
        return self.page.title

    def __unicode__(self):
        return self.page.title


class UserProfile(models.Model):
    # Required Line - links class to model instance
    user = models.OneToOneField(User)

    # Additional Attributes:
    picture = models.ImageField(upload_to='profile_images', blank=True)

    class Meta:
        verbose_name_plural = "UserProfiles"

    # __unicode__() override
    def __str__(self):
        return self.user.username

    # Defined for the sake of compatibility
    def __unicode__(self):
        return self.user.username


# YEA BOI


# Multiple comments may be posted per QuestionPost (Many to one relationship)
class Comment(models.Model):
    max_comment_length = 1024
    post = models.ForeignKey(QuestionPost)
    user_profile = models.ForeignKey(UserProfile, null=True)
    content = models.TextField(max_length=max_comment_length)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


#class Photo(models.Model):
#    post = models.ForeignKey(QuestionPost)
#    image = models.ImageField(upload_to='')
#   description = models.CharField(max_length=160)
