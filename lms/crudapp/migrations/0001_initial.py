# Generated by Django 3.2 on 2021-04-21 06:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('grade', models.IntegerField(choices=[(4, 'Grade 4'), (3, 'Grade 3'), (1, 'Grade 1'), (5, 'Grade 5'), (2, 'Grade 2')])),
                ('joining_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('SL', 'Sick Leave'), ('ML', 'Maternity Leave'), ('CL', 'Casual Leave'), ('EL', 'Earned Leave'), ('LW', 'Leave Without Pay')], max_length=2)),
                ('grade', models.IntegerField(choices=[(4, 'Grade 4'), (3, 'Grade 3'), (1, 'Grade 1'), (5, 'Grade 5'), (2, 'Grade 2')])),
                ('leave_description', models.CharField(max_length=100)),
                ('number_of_days_in_a_year', models.IntegerField()),
                ('accrual_flag', models.BooleanField(default=False)),
                ('maximum_accrual_days', models.IntegerField(default=0)),
                ('special_leave_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestID', models.IntegerField()),
                ('request_period_from', models.DateField(auto_now=True)),
                ('request_period_to', models.DateField(auto_now=True)),
                ('approved_period_from', models.DateField(auto_now=True)),
                ('approved_period_to', models.DateField(auto_now=True)),
                ('request_comments', models.CharField(blank=True, max_length=100)),
                ('approval_flag', models.BooleanField(default=False)),
                ('approved_user_comments', models.CharField(blank=True, max_length=100)),
                ('approve_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaverequest_requests_approved', to='crudapp.employee')),
                ('approved_leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaverequest_lt_approve', to='crudapp.leavemaster')),
                ('created_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaverequest_requests_created', to='crudapp.employee')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.employee')),
                ('request_leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaverequest_lt_request', to='crudapp.leavemaster')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLeaveHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Calendar_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2012), django.core.validators.MaxValueValidator(2035)])),
                ('EligibleDays', models.CharField(max_length=10)),
                ('AvailedDays', models.DecimalField(decimal_places=1, max_digits=4)),
                ('BalanceDays', models.DecimalField(decimal_places=1, max_digits=4)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.employee')),
                ('leave_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crudapp.leavemaster')),
            ],
        ),
    ]