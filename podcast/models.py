from django.db import models
from account.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class Singer(models.Model):
    name = models.CharField(max_length=300 , verbose_name='نام گوینده')
    image = models.ImageField(upload_to='podcast/singer/' , verbose_name='عکس گوینده')
    discrip = RichTextUploadingField(null=True , blank=True , verbose_name='توضیحات درباره ی گوینده' , help_text='اختیاری')
    favorite_count = models.IntegerField(default=0 , verbose_name='تعدا علاقه مندی ها')
    likes = models.ManyToManyField(User, related_name="singerlikes", default=None, blank=True , verbose_name='یوزر هایی که لایک کردند')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'گوینده  '
        verbose_name_plural = 'گوینده ها'

class Category(models.Model):
    title = models.CharField(max_length=450 , verbose_name='نام دسته بندی')
    discription = RichTextUploadingField(null=True , blank=True , verbose_name='توضیحات')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی پی')

class Podcast(models.Model):
    title = models.CharField(max_length=350 , verbose_name='نام پادکست')
    english_title = models.CharField(max_length=350 , null=True , verbose_name='نام اینگلیسی پادکست')
    slug = models.SlugField(null=True , blank=True)
    singer = models.ForeignKey(Singer , on_delete=models.CASCADE , related_name='podcasts' , verbose_name='گوینده')
    categories = models.ManyToManyField(Category , related_name='podcasts' , verbose_name='دسته بندی')
    likes = models.ManyToManyField(User, related_name="podcastlikes", default=None, blank=True , verbose_name='یوزر هایی که لایک کردند')
    saves = models.ManyToManyField(User, related_name="podcastsaves", default=None, blank=True , verbose_name='یوزر هایی که ذخیره کردند')
    cover = models.ImageField(upload_to='podcast/cover/' , verbose_name='کاور پادکست')
    podcast = models.FileField(upload_to='podcast/podcast/' , verbose_name='پادکست')
    views = models.IntegerField(default=0 , verbose_name='تعداد بازدید ها')
    fit_by = models.CharField(max_length=250 , null=True , blank=True , verbose_name='ادیت شده توسط')
    favorite_count = models.IntegerField(default=0 , verbose_name='تعدا علاقه مندی ها')
    subscription = models.BooleanField(default=False , verbose_name='ایا این پادکست جزو اهنگ های اشتراکی است ؟' , null=True)
    public = models.BooleanField(default=False , verbose_name='منتشر شده')
    private = models.BooleanField(default=False , verbose_name='خصوصی')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'پادکست'
        verbose_name_plural = 'پادکست ها'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Podcast , self).save(*args, **kwargs)

class PodcastFavorite(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='podcast_favorites' , verbose_name='کاربر')
    podcast = models.ForeignKey(Podcast , on_delete=models.CASCADE , related_name='podcast_favorites' , verbose_name='پادکست')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.podcast.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'علاقه مندی برای پادسکت'
        verbose_name_plural ='علاقه مندی ها برای پادکست'  
    
class PodcastSave(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='podcast_saves' , verbose_name='کاربر')
    podcast = models.ForeignKey(Podcast , on_delete=models.CASCADE , related_name='podcast_saves' , verbose_name='پادکست')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.podcast.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'ذخیره  برای پادسکت'
        verbose_name_plural ='ذخیره ها برای پادکست'  

class SingerFavorite(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='singer_favorites' , verbose_name='کاربر')
    singer = models.ForeignKey(Singer , on_delete=models.CASCADE , related_name='singer_favorites' , verbose_name='گوینده')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.singer.name
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'علاقه مندی برای خواننده'
        verbose_name_plural ='علاقه مندی ها برای خواننده'  

class PlayList(models.Model):
    title = models.CharField(max_length=350 , null=True ,  verbose_name='نام پلی لیست')
    cover = models.ImageField(upload_to='playlists/cover/' , verbose_name='کاور پلی لیست')
    singer = models.ForeignKey(Singer , on_delete=models.CASCADE , related_name='playlists' , verbose_name='گوینده')
    podcast = models.ManyToManyField(Podcast , related_name='playlists' , verbose_name='پادکست ها' , null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = "لیست پخش"
        verbose_name_plural = "لیست ها پخش"