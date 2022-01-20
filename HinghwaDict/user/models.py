from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info', verbose_name='用户',
                                primary_key=True)
    wechat = models.CharField(max_length=128, blank=True, verbose_name="微信标识码")  # openid
    qq = models.CharField(max_length=128, blank=True, verbose_name="qq标识码")  # openid
    nickname = models.CharField(blank=True, max_length=100, verbose_name='昵称')
    birthday = models.DateField(blank=True, default='1970-1-1', verbose_name='生日')
    telephone = models.CharField(blank=True, max_length=50, verbose_name='电话')
    avatar = models.URLField(default='https://hinghwadict-1259415432.cos.***REMOVED***.myqcloud.com/'
                                     'files/image/1/2022/01/19/bMuzwU97XtBZHve.jpg',
                             blank=True, verbose_name='头像')
    county = models.CharField(blank=True, max_length=100, verbose_name="县区")
    town = models.CharField(blank=True, max_length=100, verbose_name="乡镇")

    def __str__(self):
        return self.user.username

    def ID(self):
        return self.user.id

    class Meta:
        verbose_name_plural = '用户详细信息'
        verbose_name = '用户详细信息'
