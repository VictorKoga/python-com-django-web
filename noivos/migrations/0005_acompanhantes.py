# Generated by Django 5.1.2 on 2024-11-03 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noivos', '0004_rename_reservar_presentes_reservado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(blank=True, max_length=25, null=True)),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanhantes', to='noivos.convidados')),
            ],
        ),
    ]
