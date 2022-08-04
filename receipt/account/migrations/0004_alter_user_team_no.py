# Generated by Django 4.0.6 on 2022-08-04 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_team_board_alter_team_team_name_team_receipt_and_more'),
        ('account', '0003_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team_no',
            field=models.ForeignKey(blank=True, db_column='team_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='party.team'),
        ),
    ]
