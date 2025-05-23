# Generated by Django 5.0.3 on 2024-04-13 09:31

import users.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.user",),
            managers=[
                ("objects", users.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="attempts_count",
            field=models.PositiveIntegerField(default=0, verbose_name="попыток входа"),
        ),
        migrations.AddField(
            model_name="profile",
            name="block_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="дата блокировки"),
        ),
    ]
