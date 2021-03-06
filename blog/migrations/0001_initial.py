# Generated by Django 2.1.5 on 2019-01-19 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome do usuário')),
                ('body', models.TextField(verbose_name='conteúdo do comentário')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='data de publicação')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo do post')),
                ('body', models.TextField(verbose_name='conteudo do post')),
                ('author', models.CharField(max_length=200, verbose_name='nome do autor')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='data da publicação')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
