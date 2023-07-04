# Generated by Django 4.2.3 on 2023-07-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('replenishment', 'Пополнение'), ('debiting', 'Списание')], max_length=13, verbose_name='Вид транзакции')),
                ('sum', models.PositiveIntegerField(verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]