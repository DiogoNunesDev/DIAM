# Generated by Django 4.2 on 2023-04-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_produto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(default='images/whiteLogo.png', upload_to='images/'),
        ),
    ]
