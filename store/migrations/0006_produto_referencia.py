# Generated by Django 4.2 on 2023-04-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_ultimo_nome_staff_apelido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='referencia',
            field=models.CharField(default='0', max_length=4),
        ),
    ]