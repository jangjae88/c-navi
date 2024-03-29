# Generated by Django 2.2.4 on 2019-08-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prouser',
            name='register_date',
            field=models.DateTimeField(auto_now=True, verbose_name='등록날짜'),
        ),
        migrations.AlterField(
            model_name='prouser',
            name='password',
            field=models.CharField(max_length=10, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='prouser',
            name='user',
            field=models.CharField(max_length=10, verbose_name='사용자'),
        ),
    ]
