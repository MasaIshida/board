from django.db import models

# Create your models here.

class BoardBase(models.Model):
    board_title = models.CharField(verbose_name='掲示板タイトル',max_length=50)
    board_about = models.CharField(verbose_name='掲示板の説明',max_length=100, null=True)
    board_date = models.DateField(verbose_name='掲示板作成日',auto_now_add=True)
    post_time = models.TimeField(verbose_name='掲示板作成時間', auto_now_add=True)
    board_view = models.PositiveIntegerField(verbose_name='閲覧回数', default=0)

    def __str__(self):
        return self.board_title


class PostContents(models.Model):
    post_user = models.CharField(verbose_name='投稿者',max_length=20)
    post_title = models.CharField(verbose_name='投稿タイトル',max_length=50)
    post_date = models.DateField(verbose_name='投稿日',auto_now_add=True)
    post_time = models.TimeField(verbose_name='投稿時間', auto_now_add=True)
    post_content = models.TextField(verbose_name='投稿内容',max_length=400)
    post_category = models.ForeignKey('BoardBase', on_delete=models.CASCADE, related_name='serch_title')




