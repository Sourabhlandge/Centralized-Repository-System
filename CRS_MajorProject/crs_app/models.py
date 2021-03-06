from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
#class CustomManager(models.Manager):
 #   def get_queryset(self):
  #      return super().get_queryset().filter(status='published')

class EducationModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    link = models.URLField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   # object = CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('education_detail',args=[self.publish.year,
    #                                        self.publish.month,
    #                                        self.publish.day,
    #                                        self.slug_field])
class HealthModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    link = models.URLField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   # object = CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('health_detail', args=[self.publish.year,
    #                                            self.publish.month,
    #                                            self.publish.day,
    #                                            self.slug_field])

class AgricultureModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    link = models.URLField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   # object = CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('agriculture_detail', args=[str(self.id),
    #                                            self.publish.year,
    #                                            self.publish.month,
    #                                            self.publish.day,
    #                                            self.slug_field])

class ElectricityModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    link = models.URLField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   # object = CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('electricity_detail', args=[str(self.id),
    #                                            self.publish.year,
    #                                            self.publish.month,
    #                                            self.publish.day,
    #                                            self.slug_field])

class BusinessModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    link = models.URLField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   # object = CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('business_detail', args=[str(self.id),
    #                                             self.publish.year,
    #                                            self.publish.month,
    #                                            self.publish.day,
    #                                            self.slug_field])

class YouthModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    link = models.URLField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   # object = CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('youth_detail', args=[self.id,
    #                                            self.publish.year,
    #                                            self.publish.month,
    #                                            self.publish.day,
    #                                            self.slug_field])
class GovernmentJobsModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    link = models.URLField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   # object = CustomManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title