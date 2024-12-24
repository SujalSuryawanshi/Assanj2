# Generated by Django 5.0.3 on 2024-09-01 05:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_staller_egit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staller',
            name='least_price',
        ),
        migrations.AddField(
            model_name='menuitems',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='menuitems',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new_offer',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='staller',
            name='category',
            field=models.ManyToManyField(related_name='categor', to='core.category'),
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.IntegerField(default=100)),
                ('description', models.CharField(max_length=600)),
                ('img_link', models.CharField(max_length=1000)),
                ('aff_link', models.CharField(max_length=300)),
                ('keywords', models.CharField(max_length=300)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_raters', to=settings.AUTH_USER_MODEL)),
                ('rat_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.foo_category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rater')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'rater')},
            },
        ),
        migrations.AddField(
            model_name='rater',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='rated_raters', through='core.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
