from django.db import models
from django.utils import timezone

class Post(models.Model):
	#author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	date = models.CharField(max_length=1,default='0')
	location = models.CharField(max_length=200,default='location')
	location_howto = models.CharField(max_length=200,default='location')
	score_k =models.CharField(max_length=20,default='0')
	score_y = models.CharField(max_length=20,default='0')
	def __str__(self):
		return self.title

class Cheeringsongs(models.Model):
	title = models.CharField(max_length=200)
	lyric = models.TextField()
	song_url = models.CharField(max_length=512)
	def __str__(self):
		return self.title

class Video(models.Model):
	title = models.CharField(max_length=200)
	video_url = models.CharField(max_length=512)
	def __str__(self):
		return self.title

class Message(models.Model):

	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
#	published_date = models.DateTimeField(blank=True,null=True)

	def __str__(self):
		return self.title

#class AfterParty(models.Model) :
#    name = models.CharField(max_length=20)
#    location = models.CharField(max_length=200)
#    def __str__(self):
#        return self.name