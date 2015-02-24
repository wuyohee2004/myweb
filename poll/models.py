from django.db import models
from django.contrib.auth.models import User

class IP(models.Model):
    hostname = models.CharField(max_length=50,unique=True)
    IP = models.IPAddressField(unique=True)
    group = models.ManyToManyField('Group',null=True,blank=True)
    port = models.IntegerField(default='22')
    os = models.CharField(max_length=20,default='linux',verbose_name='Operating System')
    def __unicode__(self):
        return self.hostname

class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.name

class RemoteUser(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.name

class PollUser(models.Model):
    user = models.ForeignKey(User,null=True)
    email = models.EmailField()
    remoteuser = models.ManyToManyField(RemoteUser,null=True,blank=True)
    group = models.ManyToManyField(Group,null=True,blank=True)
    ip = models.ManyToManyField(IP,null=True,blank=True)
    def __unicode__(self):
        return '%s' % self.user

class AuthByIpAndRemoteUser(models.Model):
    password = models.CharField(max_length=1024,verbose_name="Password or SSL_KEY")
    AUTH_CHOICES = (('ssh','ssh-password'),('ssh-key','ssh-key'))
    authtype = models.CharField(max_length=100,choices=AUTH_CHOICES)
    ip = models.ForeignKey(IP,null=True,blank=True)
    remoteUser = models.ForeignKey(RemoteUser,null=True,blank=True)
    def __unicode__(self):
        return '%s\t%s' %(self.ip,self.remoteUser)
    class Meta:
        unique_together = (('ip','remoteUser'),)

class OpsLog(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True,blank=True)
    log_type = models.CharField(max_length=50)
    poll_user = models.CharField(max_length=30)
    run_user = models.CharField(max_length=30)
    cmd = models.TextField()
    total_task = models.IntegerField()
    success_num = models.IntegerField()
    failed_num = models.IntegerField()
    track_mark = models.IntegerField(unique=True)
    note = models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.cmd

class OpsLogTemp(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=30)
    ip = models.IPAddressField()
    event_type = models.CharField(max_length=50)
    cmd = models.TextField()
    event_log = models.TextField()
    result = models.CharField(max_length=30,default='unknown')
    track_mark = models.IntegerField(blank=True)
    note = models.CharField(max_length=100,blank=True)
    def __unicode__(self):
        return self.ip

# Create your models here.
# class Publisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.URLField()
#     def __unicode__(self):
#         return self.name
# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#     def __unicode__(self):
#         return self.first_name
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()
#     def __unicode__(self):
#         return self.title

