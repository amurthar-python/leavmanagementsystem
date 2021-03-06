# Generated by Django 3.2 on 2021-04-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_auto_20210421_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='grade',
            field=models.IntegerField(choices=[(1, 'Grade 1'), (4, 'Grade 4'), (5, 'Grade 5'), (2, 'Grade 2'), (3, 'Grade 3')]),
        ),
        migrations.AlterField(
            model_name='leavemaster',
            name='grade',
            field=models.IntegerField(choices=[(1, 'Grade 1'), (4, 'Grade 4'), (5, 'Grade 5'), (2, 'Grade 2'), (3, 'Grade 3')]),
        ),
        migrations.AlterField(
            model_name='leavemaster',
            name='leave_type',
            field=models.CharField(choices=[('SL', 'Sick Leave'), ('ML', 'Maternity Leave'), ('EL', 'Earned Leave'), ('LW', 'Leave Without Pay'), ('CL', 'Casual Leave')], max_length=2),
        ),
    ]
