# Generated by Django 2.2 on 2020-07-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_page_meta", "0011_auto_20190218_1010"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pagemeta",
            name="gplus_author",
        ),
        migrations.RemoveField(
            model_name="pagemeta",
            name="gplus_type",
        ),
        migrations.RemoveField(
            model_name="titlemeta",
            name="gplus_description",
        ),
        migrations.AddField(
            model_name="pagemeta",
            name="schemaorg_type",
            field=models.CharField(
                blank=True, help_text="Use Article for generic pages.", max_length=255, verbose_name="Resource type"
            ),
        ),
    ]
