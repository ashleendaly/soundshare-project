# Generated by Django 2.2.26 on 2022-03-07 04:26

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_text', models.CharField(max_length=64)),
                ('email_text', models.CharField(max_length=64)),
                ('password_text', models.CharField(max_length=64)),
                ('firstname_text', models.CharField(max_length=64)),
                ('lastname_text', models.CharField(max_length=64)),
                ('image', models.ImageField(default='images/default.png', max_length=200, upload_to='images/%Y/%m', verbose_name='Profile photo')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
