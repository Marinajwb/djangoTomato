from django.db import models

class Post(models.Model):
    #하나의 글에 여러 이미지와 댓글이 연결
    # ForeignKey를 사용해 다대일 관계구성
    user = models.ForeignKey(
        'users.User',
        verbose_name= '작성자',
        on_delete=models.CASCADE,
    )
    content = models.TextField('내용')
    create  = models.DateTimeField('생성일시', auto_now_add=True)

class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name= '포스트',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(
        '사진',
        upload_to = 'posts',
    )

class Comment(models.Model):
     user = models.ForeignKey(
         'users.User',
         verbose_name = '작성자',
         on_delete = models.CASCADE,
     )
     post    = models.ForeignKey(Post, verbose_name='포스트', on_delete=models.CASCADE)
     content = models.TextField('내용')
     created = models.DateTimeField('생성일시', auto_now_add=True)