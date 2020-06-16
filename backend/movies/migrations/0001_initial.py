# Generated by Django 3.0.2 on 2020-06-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('original_title', models.CharField(max_length=100)),
                ('poster', models.URLField()),
                ('background', models.URLField()),
                ('vote_average', models.FloatField()),
                ('release_date', models.DateField()),
                ('content', models.TextField()),
                ('tagline', models.CharField(max_length=255)),
                ('runtime', models.IntegerField()),
                ('tmdb_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('movie', models.ManyToManyField(blank=True, related_name='genres', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('movie', models.ManyToManyField(blank=True, related_name='countries', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('biography', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('gender', models.IntegerField()),
                ('birthday', models.DateField()),
                ('profile', models.URLField()),
                ('place_of_birth', models.CharField(max_length=255)),
                ('cast_id', models.IntegerField(unique=True)),
                ('movie', models.ManyToManyField(blank=True, related_name='casts', to='movies.Movie')),
            ],
        ),
    ]
