# Generated by Django 4.1.2 on 2022-10-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archive", "0004_redirect"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redirect",
            name="old",
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
