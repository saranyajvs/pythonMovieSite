# Generated by Django 4.1.7 on 2023-04-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movies_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='Movie')),
            ],
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
