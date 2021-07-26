from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,     # User 모델과 1:1 관계를 만겠다. 외래키 설정
                                related_name='profile')             # related_name: User가 이 Profile 모델을 어떤 이름으로 바라볼 것인가
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True)
    message = models.CharField(max_length=255, null=True)
