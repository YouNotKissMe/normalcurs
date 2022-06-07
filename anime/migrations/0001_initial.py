# Generated by Django 4.0.5 on 2022-06-07 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('an', models.CharField(max_length=100, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('about', models.TextField(verbose_name='Описание')),
                ('trailer', models.FileField(blank=True, null=True, upload_to='', verbose_name='Трейлер')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Заглавная картинка')),
                ('links', models.TextField(blank=True, null=True, verbose_name='Ссылки на источники для просмотра аниме')),
                ('anime', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.genre', verbose_name='Жанр')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anonce', verbose_name='Статус')),
                ('typeAnime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Аниме',
                'verbose_name_plural': 'Аниме',
            },
        ),
    ]