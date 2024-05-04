from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    dd = 'DAMAGEDILLER'
    tk = 'TANK'
    hl = 'HEALER'
    tr = 'TRADER'
    gm = 'GILDMASTER'
    qg = 'QUESTGIVER'
    bs = 'BLACKSMITH'
    tn = 'TANNER'
    pm = 'POTIONMAKER'
    sm = 'SPELLMASTER'

    CATEGORY_TYPES = [
        (dd, 'ДД'),
        (tk, 'Танк'),
        (hl, 'Хил'),
        (tr, 'Торговец'),
        (gm, 'Гильдмастер'),
        (qg, 'Квестгивер'),
        (bs, 'Кузнец'),
        (tn, 'Кожевник'),
        (pm, 'Зельевар'),
        (sm, 'Мастер заклинаний'),
    ]

    name = models.CharField(max_length=17, choices=CATEGORY_TYPES)

    def __str__(self):
        return self.name.title()



class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title.title()


class Replay(models.Model):
    replay_author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)# статус отклика по умолчанию False
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

