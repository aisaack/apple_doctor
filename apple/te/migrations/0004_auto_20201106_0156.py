# Generated by Django 3.1.2 on 2020-11-06 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('te', '0003_auto_20201103_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=250, unique=True)),
                ('slug', models.SlugField(default=None, max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'verbose_name': 'disease', 'verbose_name_plural': 'diseases'},
        ),
        migrations.RemoveField(
            model_name='disease',
            name='content',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='title',
        ),
        migrations.AddField(
            model_name='disease',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='image',
            field=models.ImageField(blank=True, upload_to='disease'),
        ),
        migrations.AddField(
            model_name='disease',
            name='name',
            field=models.CharField(default=None, max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='pest',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='slug',
            field=models.SlugField(default=None, max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='symptom',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='te.category'),
            preserve_default=False,
        ),
    ]