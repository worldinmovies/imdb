# Generated by Django 4.1.5 on 2023-01-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_set_imdb_id_to_blankeable_and_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(db_index=True, max_length=30, null=True),
        ),
    ]
