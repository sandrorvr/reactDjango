# Generated by Django 4.1.4 on 2023-01-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_general', '0003_alter_servidor_parceiro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roteiro',
            old_name='roteiro',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='roteiro',
            name='id',
        ),
        migrations.RemoveField(
            model_name='roteiro',
            name='matricula',
        ),
        migrations.AddField(
            model_name='roteiro',
            name='cod_roteiro',
            field=models.CharField(default=1, max_length=5, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]