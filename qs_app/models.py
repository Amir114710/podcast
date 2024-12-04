from django.db import models

# class User(AbstractUser):
#     Choices1=(
#         ('مادر' ,'مادر'),
#         ('پدر', 'پدر'),
#         ('دانش اموز', 'دانش اموز')
#     )
#     Choices2=(
#         ('هفتم' ,'هفتم'),
#         ('هشتم', 'هشتم'),
#         ('نهم', 'نهم')
#     )
#     Ratio = models.CharField(max_length=100 , help_text="", choices=Choices1 , default='مادر')
#     the_base = models.CharField(max_length=100 , help_text="", choices=Choices2 , default='مادر')
#     number = models.IntegerField(default=58)
#     image = models.ImageField(null=True, help_text="", upload_to='UserProfile')   

class Question(models.Model):
    qs = models.TextField(null=True , blank=True , verbose_name='سوال')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.qs
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'

class Options(models.Model):
    option = models.CharField(max_length=650 , null=True , blank=True , verbose_name='گزینه')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.option
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'گزینه'
        verbose_name_plural = 'گزینه ها'

class MainQuestion(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE , related_name='mainqs' , null=True , verbose_name='سوال')
    option1 = models.ForeignKey(Options , on_delete=models.CASCADE , related_name='mainqs1' , verbose_name='گزینه 1')
    option2 = models.ForeignKey(Options , on_delete=models.CASCADE , related_name='mainqs2' , verbose_name='گزینه 2')
    option3 = models.ForeignKey(Options , on_delete=models.CASCADE , related_name='mainqs3' , verbose_name='گزینه 3')
    option4 = models.ForeignKey(Options , on_delete=models.CASCADE , related_name='mainqs4' , verbose_name='گزینه 4')
    correct_option = models.ForeignKey(Options , on_delete=models.CASCADE , related_name='mainqs_correct' , verbose_name='گزینه درست')
    correct_count = models.IntegerField(null=True , blank=True , verbose_name='تعداد درست')
    uncorrect_count = models.IntegerField(null=True , blank=True , verbose_name='تعداد نادرست')
    null_count = models.IntegerField(null=True , blank=True , verbose_name='تعداد بدون جواب')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'سوال اصلی'
        verbose_name_plural = 'سوالات اصلی'