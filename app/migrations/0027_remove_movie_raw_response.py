# Generated by Django 4.1.5 on 2023-03-30 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0026_change_raw_response_from_dict_to_json"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="raw_response",
        ),
    ]
