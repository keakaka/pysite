from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)
    groupno = models.IntegerField(default=0)
    orderno = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    status = models.CharField(max_length=1, default='Y')
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.title}, {self.content}, {self.hit}, {self.regdate}, {self.groupno}, {self.orderno}, {self.depth}, {self.status}, {self.user})'
