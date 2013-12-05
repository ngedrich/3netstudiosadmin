from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Format(models.Model):
	name = models.CharField(max_length=20)
	def __unicode__(self):
		return self.name

class Show(models.Model):
	title = models.CharField(max_length=200)
	runtime = models.CharField(max_length=50)
	category = models.ForeignKey(Category)
	formats = models.ManyToManyField(Format)
	homePageThumbNail = models.ImageField(upload_to='images/HomePageThumbnail/')
	detailMarqueeImage = models.ImageField(upload_to='images/DetailMarquee/')
	details = models.TextField()
	videoPlaylistID = models.CharField(max_length=200)
	sortOrder = models.IntegerField()
	def __unicode__(self):
		return self.title

class Photo(models.Model):
	show = models.ForeignKey(Show)
	image = models.ImageField(upload_to='images/showPhotos/')
	caption = models.CharField(max_length=200)

