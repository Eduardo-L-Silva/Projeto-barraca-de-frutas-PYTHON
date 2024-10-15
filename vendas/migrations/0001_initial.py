# Generated by Django 5.0.7 on 2024-07-27 01:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('classificacao', models.CharField(choices=[('extra', 'Extra'), ('primeira', 'De Primeira'), ('segunda', 'De Segunda'), ('terceira', 'De Terceira')], max_length=10)),
                ('fresca', models.BooleanField(default=True)),
                ('quantidade_disponivel', models.PositiveIntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desconto', models.PositiveIntegerField(default=0)),
                ('fruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.fruta')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]