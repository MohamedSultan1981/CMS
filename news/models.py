from django.db import models
from datetime import datetime,date
from tinymce.models import HTMLField
from django.urls import reverse
from django.contrib.auth.models import User
#from thumbnails.fields import ImageField
from django.core.files.storage import FileSystemStorage
#from django.dispatch import receiver
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.alias import aliases
from django.utils.text import slugify 
import arabic_reshaper
from bidi.algorithm import get_display



if not aliases.get('badge'):
    aliases.set('badge', {'size': (150, 80), 'crop': True})
saved_file.connect(generate_aliases_global)   



class NewsType(models.Model):
    newsName=models.CharField("نوع الخبر",max_length=200)
    def __str__(self):
        return self.newsName
    class Meta(object):
        
        verbose_name_plural="انواع الاخبار"
        verbose_name="نوع الخبر"  
          
class PaperType(models.Model):
    paperName=models.CharField("الجريدة",max_length=200)
    def __str__(self):
        return self.paperName
    class Meta(object):
        
        verbose_name_plural="الجرائد"
        verbose_name="جريدة"
#------------------------------------------------------------------------------------------- 
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.STATUS_CHOICES.PUBLISHED)
class News(models.Model):
    class STATUS_CHOICES(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        WITHDRAW='WD','Withdraw'
    title=models.CharField("العنوان",max_length=1500)
    newstype=models.ForeignKey(NewsType, on_delete=models.CASCADE, null=True, verbose_name="نوع الخبر", blank=True  ) 
    papertype=models.ManyToManyField( PaperType, null=True, verbose_name="الجريدة", blank=True )
    negative=models.BooleanField("سلبي")
    newsscript=HTMLField("تفاصيل الخبر",blank=True, null=True)
    newsdate=models.DateField("تاريخ نشر الخبر")
    newsurl=models.URLField("رابط الخبر",blank=True,null=True, max_length=1500)
    slug=models.SlugField("العنوان الذي يظهرفي الرابط",allow_unicode=True ,null=False,blank=False, unique=False,unique_for_date='newsdate',max_length=1500)
    newsvideo = models.FileField("رابط وسائط متعددة عن الخبر",blank=True, null=True, upload_to='video/')
    newsembedvideo=models.TextField("تضمين وسائط متعددة عن الخبر مثل 'YOUTUBE'",blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ ادخال الخبر")
    updated_at = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False ,verbose_name="ترتيب الأخبار")
    status = models.CharField("حالة الخبر",max_length=2, choices=STATUS_CHOICES.choices,default=STATUS_CHOICES.DRAFT)
    objects = models.Manager() # The default manager.
    published = PublishedManager()
    class Meta(object):
        ordering = ['my_order']
        verbose_name_plural="الاخبار"
        verbose_name="خبر"
        managed=True
        db_table='news_news'
    
        
    # def save(self, *args, **kwargs):
    #     reshaped_text=arabic_reshaper.reshape(slugify(self.title,allow_unicode=True))
    #     bidi_text = get_display(reshaped_text)
    #     self.slug = bidi_text
    #     super().save(*args, **kwargs)
    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        #return reverse("news:news-detail", kwargs={'slug': self.slug})
        #return reverse("news:news-detail", kwargs={'pk': self.pk})
        return reverse("news:news-detail",args=[self.newsdate.year,self.newsdate.month,self.newsdate.day,self.slug])
   
  
class NewsFile(models.Model):
    filename=models.FileField("الملف",blank=True, null=True)
    newsid=models.ForeignKey(News,on_delete=models.CASCADE,related_name="News_file")
    def __str__(self):
        return str(self.filename)
    class Meta(object):
        
        verbose_name_plural="الملفات"
        verbose_name="ملف"

class Newsimages(models.Model):
    #filename=ImageField(storage=FileSystemStorage())
    image=models.ImageField("الصورة",upload_to = 'photo/', blank=True,null=True )
    newsid=models.ForeignKey(News,on_delete=models.CASCADE,related_name="News_image")
    
    def __str__(self):
        return str(self.image)
    class Meta(object):
        managed = True
        db_table = 'news_newsimages'
        verbose_name_plural="الصور"
        verbose_name="صورة"        