# Generated by Django 5.0.6 on 2024-07-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lc_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LetterOfCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_number', models.CharField(max_length=20, unique=True)),
                ('applicant_name', models.CharField(max_length=100)),
                ('beneficiary_name', models.CharField(max_length=100)),
                ('issuing_bank', models.CharField(max_length=100)),
                ('advising_bank', models.CharField(max_length=100)),
                ('negotiating_bank', models.CharField(max_length=100)),
                ('confirming_bank', models.CharField(max_length=100)),
                ('lc_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(choices=[('NOT APPROVED', 'NOT APPROVED'), ('APPROVED', 'APPROVED')], max_length=20)),
            ],
        ),
    ]
