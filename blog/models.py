from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('titulo do post', max_length=200)
    body = models.TextField('conteudo do post')
    author = models.CharField('nome do autor', max_length=200)
    pub_date = models.DateTimeField('data da publicação', auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField('nome do usuário',max_length=100)
    body = models.TextField('conteúdo do comentário')
    pub_date = models.DateTimeField('data de publicação', auto_now=True)
