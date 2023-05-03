# Generated by Django 4.2 on 2023-05-03 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0019_produto_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="carrinhocompras",
            name="utilizador",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.utilizador",
            ),
        ),
        migrations.CreateModel(
            name="carrinhoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade", models.IntegerField(default=1)),
                (
                    "carrinho",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.carrinhocompras",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.produto"
                    ),
                ),
            ],
        ),
    ]
