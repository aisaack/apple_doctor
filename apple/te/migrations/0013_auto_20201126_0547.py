# Generated by Django 3.1.2 on 2020-11-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('te', '0012_auto_20201113_0830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pest',
            options={},
        ),
        migrations.AlterField(
            model_name='pest',
            name='diseaseWeedName',
            field=models.CharField(default=None, max_length=250, verbose_name='적용병해충'),
        ),
    ]