# Generated by Django 4.2.5 on 2023-09-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("offer", "0011_rangeproductfileupload_included"),
    ]

    operations = [
        migrations.CreateModel(
            name="FixedUnitDiscountBenefit",
            fields=[],
            options={
                "verbose_name": "Fixed unit discount benefit",
                "verbose_name_plural": "Fixed unit discount benefits",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("offer.absolutediscountbenefit",),
        ),
        migrations.AlterField(
            model_name="benefit",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Percentage",
                        "Discount is a percentage off of the product's value",
                    ),
                    (
                        "Absolute",
                        "Discount is a fixed amount off of the basket's total",
                    ),
                    ("Fixed", "Discount is a fixed amount off of the product's value"),
                    ("Multibuy", "Discount is to give the cheapest product for free"),
                    (
                        "Fixed price",
                        "Get the products that meet the condition for a fixed price",
                    ),
                    (
                        "Shipping absolute",
                        "Discount is a fixed amount of the shipping cost",
                    ),
                    ("Shipping fixed price", "Get shipping for a fixed price"),
                    (
                        "Shipping percentage",
                        "Discount is a percentage off of the shipping cost",
                    ),
                ],
                max_length=128,
                verbose_name="Type",
            ),
        ),
    ]