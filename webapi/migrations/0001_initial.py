# Generated by Django 3.2.6 on 2021-08-31 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('data_type', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=30)),
                ('project_code', models.UUIDField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('environment', models.PositiveSmallIntegerField()),
                ('default_value', models.PositiveSmallIntegerField()),
                ('rollout_threshold', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_id', to='webapi.feature')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.stream')),
            ],
        ),
        migrations.CreateModel(
            name='ExpressionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('value', models.PositiveSmallIntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('changed_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.feature')),
            ],
        ),
    ]