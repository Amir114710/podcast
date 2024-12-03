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