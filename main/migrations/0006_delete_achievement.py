from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_project"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Achievement",
        ),
    ]
