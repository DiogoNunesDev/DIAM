# Generated by Django 4.2 on 2023-05-01 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_comentario_referencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='utilizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.utilizador'),
        ),
    ]
