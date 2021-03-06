from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

class Job(models.Model):
    job_author = models.ForeignKey('auth.User',blank=True,null=True)
    job_company = models.ForeignKey('companies.Company',default=0)
    job_location = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_types_choices = (
        ('full_time','Full Time'),
        ('part_time','Part Time'),
        ('contract','Contract'),
        ('internship','Internship')
    )
    job_type = models.CharField(max_length=20,choices=job_types_choices,default='full_time')
    job_description = models.TextField(default='')
    job_responsibilities = models.TextField(default='')
    job_qualifications = models.TextField(default='')
    job_notes = models.TextField(default='')
    job_created_date = models.DateTimeField('date created',auto_now_add=True,null=True)
    job_expiration_date = models.DateTimeField(default=timezone.now() + timedelta(days=60))
    job_status_choices = (
        ('draft','Draft'),
        ('pending_review','Pending Review'),
        ('published','Published'),
        ('filled','Filled'),
    )
    job_status = models.CharField(max_length="20",choices=job_status_choices,default='draft')
    job_apply_method_choices = (
        ('link','Link'),
        ('email','Email'),
    )
    job_apply_method = models.CharField(max_length="20",choices=job_apply_method_choices,default='draft')
    job_apply_link = models.CharField(max_length=400,default='')
    tags = TaggableManager()


    def __unicode__(self):
        return self.job_status

    def get_absolute_url(self):
        return '/jobs/%i/' % (self.id)
