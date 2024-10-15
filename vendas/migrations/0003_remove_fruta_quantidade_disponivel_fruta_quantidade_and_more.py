# Generated by Django 5.0.7 on 2024-07-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_rename_data_hora_venda_horario_venda_quantidade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruta',
            name='quantidade_disponivel',
        ),
        migrations.AddField(
            model_name='fruta',
            name='quantidade',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fruta',
            name='classificacao',
            field=models.CharField(choices=[('EX', 'Extra'), ('PR', 'De Primeira'), ('Se', 'De Segunda'), ('Tr', 'De Terceira')], max_length=2),
        ),
        migrations.AlterField(
            model_name='fruta',
            name='fresca',
            field=models.BooleanField(default=True),
        ),
    ]
