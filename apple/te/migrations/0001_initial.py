# Generated by Django 3.1.2 on 2020-10-15 05:46

from django.db import migrations, models
import te.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=te.models.date_upload_to)),
            ],
        ),
    ]