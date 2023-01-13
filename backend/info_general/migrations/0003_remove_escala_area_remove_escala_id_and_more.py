# Generated by Django 4.1.4 on 2023-01-11 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info_general', '0002_alter_escala_cod_guarnica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escala',
            name='area',
        ),
        migrations.RemoveField(
            model_name='escala',
            name='id',
        ),
        migrations.RemoveField(
            model_name='escala',
            name='posto_base',
        ),
        migrations.AddField(
            model_name='escala',
            name='cod_escala',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escala',
            name='cod_local',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info_general.local'),
            preserve_default=False,
        ),
    ]