# Generated by Django 5.0.6 on 2024-06-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_profile_name_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
