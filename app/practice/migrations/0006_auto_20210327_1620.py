# Generated by Django 3.1.7 on 2021-03-27 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('practice', '0005_auto_20210324_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisereport',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='profile.user', verbose_name='ученик'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exerciseansweroption',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='practice.exercise', verbose_name='задание'),
        ),
    ]