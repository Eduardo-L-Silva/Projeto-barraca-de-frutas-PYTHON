# Generated by Django 5.0.7 on 2024-07-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_remove_fruta_quantidade_disponivel_fruta_quantidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruta',
            name='classificacao',
            field=models.CharField(choices=[('EX', 'Extra'), ('1', 'De Primeira'), ('2', 'De Segunda'), ('3', 'De Terceira')], max_length=2),
        ),
    ]
