# Generated by Django 5.0.2 on 2024-03-10 01:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0004_transaction_borrowing_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="borrow_book",
            field=models.BooleanField(default=False),
        ),
    ]
