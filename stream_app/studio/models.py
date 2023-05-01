from django.db import models
from app_users.models import Users

class Stream(models.Model):
    title=models.CharField(max_length=255,default='')
    time_update=models.DateTimeField(auto_now=True, null=True)
    is_online=models.BooleanField(default=False)
    # autor=models.ForeignKey('Users' )
    

