"""Initial migration for Character model."""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Initial migration class."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('character', models.CharField(max_length=100)),
                ('pinyin', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('correct_count', models.PositiveIntegerField(default=0)),
                ('incorrect_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
