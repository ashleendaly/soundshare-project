# Generated by Django 2.2.26 on 2022-03-18 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soundshare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('average_rating', models.IntegerField(default=0)),
                ('link', models.URLField(unique=True)),
                ('creator', models.ManyToManyField(to='soundshare.UserProfile')),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=10000)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soundshare.Album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soundshare.Song')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soundshare.UserProfile')),
            ],
        ),
    ]