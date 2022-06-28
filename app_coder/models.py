from django.contrib.auth.models import User
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=40)
    sub_title = models.CharField(max_length=40)
    text = models.TextField()
    image = models.ImageField(upload_to='articles', null=True, blank=True)

    def __str__(self):
        return f'{self.title} -- {self.sub_title}'

class Comments(models.Model):
    data = models.TextField()
    due_date = models.DateTimeField(auto_now_add=True, null=False)
    article = models.ForeignKey (Articles, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario: {self.data} -- Fecha del comentario: {self.due_date}'


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'
