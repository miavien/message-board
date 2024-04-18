# Generated by Django 5.0.4 on 2024-04-18 11:05

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('DD', 'ДД'), ('TANK', 'Танк'), ('HEAL', 'Хил'), ('TREADER', 'Торговец'), ('GUILDMASTER', 'Гилдмастер'), ('QUESTGIVER', 'Квестгивер'), ('BLACKSMITH', 'Кузнец'), ('TANNER', 'Кожевник'), ('POTIONEER', 'Зельевар'), ('SPELLMASTER', 'Мастер заклинаний')], default='DD', max_length=11)),
                ('subscribers', models.ManyToManyField(blank=True, null=True, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_in', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default='DD', on_delete=django.db.models.deletion.CASCADE, to='mmo.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_in', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmo.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
