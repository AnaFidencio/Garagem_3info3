# Generated by Django 5.0.2 on 2024-04-08 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_categoria_cor_marca_rename_nome_acessorio_descrição"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cor",
            old_name="descrição",
            new_name="nome",
        ),
    ]
