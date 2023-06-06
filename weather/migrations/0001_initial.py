# Generated by Django 4.2.2 on 2023-06-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='yearly_temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('jan_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('feb_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('mar_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('apr_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('may_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('jun_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('jul_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('aug_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sep_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('oct_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('nov_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('dec_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('win_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('spr_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sum_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('aut_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('ann_temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
    ]