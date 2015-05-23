from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()

    def __unicode__(self):
        return self.titulo
