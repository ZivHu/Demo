# Generated by Django 2.0.7 on 2018-08-08 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_reviewstatus_statusoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='角色名称')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='用户')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.RemoveField(
            model_name='reviewstatus',
            name='user',
        ),
        migrations.RemoveField(
            model_name='statusoption',
            name='status',
        ),
        migrations.DeleteModel(
            name='ReviewStatus',
        ),
        migrations.DeleteModel(
            name='StatusOption',
        ),
    ]
