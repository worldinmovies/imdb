# Generated by Django 4.1.5 on 2023-01-23 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_movie_imdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativetitle',
            name='movie',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='alternative_titles', to='app.movie'),
        ),
    ]
