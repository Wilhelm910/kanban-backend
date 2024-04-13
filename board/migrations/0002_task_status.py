# Generated by Django 5.0.4 on 2024-04-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'To Do'), ('doing', 'Doing'), ('review', 'Review'), ('done', 'Done')], default='todo', max_length=10),
        ),
    ]