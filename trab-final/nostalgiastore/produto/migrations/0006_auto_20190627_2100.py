# Generated by Django 2.2.1 on 2019-06-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_produto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]