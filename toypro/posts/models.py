from django.db import models
from toypro.users import models as user_model
# Create your models here. 
#데이터의 생성 및 수정 시간 추상형으로 두어 생성시키지 않고 상속용으로만 사용
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True) 
    updated_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        abstract = True 


class Posts(TimeStampedModel):
    author = models.ForeignKey(
        user_model.User, 
        null=True,
        on_delete=models.CASCADE, #유저가 삭제되면 캐스케이드
        related_name='post_author'
    )
    image =models.ImageField(blank=True)
    caption =models.TextField(blank=True)
    like_image= models.ManyToManyField(user_model.User, related_name='post_image_likes')
class Comments(TimeStampedModel):
    author = models.ForeignKey(
        user_model.User, 
        null=True,
        on_delete=models.CASCADE, #유저가 삭제되면 캐스케이드
        related_name='comment_author'
    )
    post = models.ForeignKey(
        Posts, 
        null=True,
        on_delete=models.CASCADE, #유저가 삭제되면 캐스케이드
        related_name='comment_post'
    )
    contents = models.TextField(blank  = True)


#작성자는 원래 models.py의 user이므로 외래키를 사용한다.