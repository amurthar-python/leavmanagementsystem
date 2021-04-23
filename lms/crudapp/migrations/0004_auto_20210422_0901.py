# Generated by Django 3.2 on 2021-04-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_auto_20210421_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='grade',
            field=models.IntegerField(choices=[(1, 'Grade 1'), (4, 'Grade 4'), (5, 'Grade 5'), (3, 'Grade 3'), (2, 'Grade 2')]),
        ),
        migrations.AlterField(
            model_name='leavemaster',
            name='grade',
            field=models.IntegerField(choices=[(1, 'Grade 1'), (4, 'Grade 4'), (5, 'Grade 5'), (3, 'Grade 3'), (2, 'Grade 2')]),
        ),
        migrations.AlterField(
            model_name='leavemaster',
            name='leave_type',
            field=models.CharField(choices=[('LW', 'Leave Without Pay'), ('EL', 'Earned Leave'), ('ML', 'Maternity Leave'), ('SL', 'Sick Leave'), ('CL', 'Casual Leave')], max_length=2),
        ),
    ]
