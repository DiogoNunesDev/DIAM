# Generated by Django 4.2 on 2023-04-30 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_produto_referencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=2000)),
                ('data', models.DateField()),
                ('utilizador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.utilizador')),
            ],
        ),
    ]
