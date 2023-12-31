# Generated by Django 5.0 on 2023-12-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("topic", models.CharField(max_length=120)),
                ("number_of_qus", models.IntegerField()),
                ("time", models.IntegerField(help_text="duration of the quiz")),
                (
                    "requierd_score_to_pass",
                    models.IntegerField(help_text="requierd socre inn %"),
                ),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("easy", "easy"),
                            ("medium", "medium"),
                            ("hard", "hard"),
                        ],
                        max_length=7,
                    ),
                ),
            ],
        ),
    ]
