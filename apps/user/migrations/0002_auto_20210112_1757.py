# Generated by Django 3.0.8 on 2021-01-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='Store/user_picture', verbose_name='アバター'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='アクティブ状態'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='ニックネーム'),
        ),
    ]
