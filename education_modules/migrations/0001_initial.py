# Generated by Django 4.2.7 on 2023-11-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('order_number', models.PositiveIntegerField(
                    unique=True,
                    verbose_name='Порядковый номер')),
                ('title', models.CharField(max_length=255,
                                           verbose_name='Название')),
                ('description', models.TextField(
                    verbose_name='Описание')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Дата создания')),
                ('is_active', models.BooleanField(
                    default=True,
                    verbose_name='Активный курс')),
                ('avatar', models.ImageField(
                    blank=True, null=True,
                    upload_to='avatars/', verbose_name='Аватар')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('text', models.TextField(
                    verbose_name='Текст отзыва')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Дата и время создания')),
            ],
        ),
    ]