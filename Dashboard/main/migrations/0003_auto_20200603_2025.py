# Generated by Django 3.0.6 on 2020-06-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200603_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceclaim',
            name='affected_body_part',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='employee_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='injury_disease',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='med_prac_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='med_prac_expertise',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='medical_assistance_req',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='name_of_reported_med_prac',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_eight',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_five',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_four',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_one',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_seven',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_six',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_three',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='test_two',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insuranceclaim',
            name='witness_present',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
