
from django.db import models
from django.contrib.auth import get_user_model
import requests
from django.utils.text import slugify
import misaka
from django import template,forms


# Create your models here.

register=template.Library()
User=get_user_model()


class Analysis(models.Model):
    user=models.ForeignKey(User,related_name='analysis',on_delete=models.CASCADE)
    topic=models.CharField(('Please enter a valid subreddit name(e.g. Coronavirus , politics , news'),max_length=300)
    score = models.CharField(('0,0'),max_length=300)
    title = models.CharField(('ahmet'), max_length = 500)
    analysis_positive=models.IntegerField(blank=False, null=False)
    analysis_negative=models.IntegerField(blank=False,null=False)
    analysis_neutral=models.IntegerField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now=True)
    CHOICES2=[('all','all'),('day','day'),('hour','hour'),('month','month'),('week','week'),('year','year')]
    limit = models.IntegerField('How many posts to visualize')
    time_filter=models.CharField('Reddit API time interval',choices=CHOICES2,max_length=300)

    class Meta():
         ordering = ['-created_at']
