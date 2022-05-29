# Generated by Django 4.0.1 on 2022-01-12 13:12

from django.db import migrations

import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0009_2_6"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="balance",
            field=djstripe.fields.StripeQuantumCurrencyAmountField(
                blank=True, default=0, null=True
            ),
        ),
    ]