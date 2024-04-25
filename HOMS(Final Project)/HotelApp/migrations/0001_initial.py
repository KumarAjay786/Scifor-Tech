# Generated by Django 5.0.4 on 2024-04-06 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Employee',
            fields=[
                ('Employee_Id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=255)),
                ('Last_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255, unique=True)),
                ('Mobile_Number', models.IntegerField(unique=True)),
                ('Joining_Date', models.CharField(max_length=255)),
                ('Dateof_Birth', models.CharField(max_length=255)),
                ('Departments', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('Blood_Group', models.CharField(max_length=255)),
                ('Education', models.CharField(max_length=255)),
                ('Personal_Identity', models.CharField(max_length=255, unique=True)),
                ('Guardian', models.CharField(max_length=255)),
                ('Guardian_Number', models.IntegerField()),
                ('Upload_Image', models.ImageField(upload_to='')),
                ('Address', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Add_Employees',
            },
        ),
        migrations.CreateModel(
            name='Add_Room',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Room_Number', models.CharField(max_length=255, unique=True)),
                ('Room_Type', models.CharField(max_length=255)),
                ('Room_Floor', models.CharField(max_length=255)),
                ('Room_Facility', models.CharField(max_length=500)),
                ('Room_Price', models.CharField(max_length=255)),
                ('Room_Image', models.ImageField(upload_to='')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Add_Room',
            },
        ),
        migrations.CreateModel(
            name='Authorregis',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=255)),
                ('Lname', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255, unique=True)),
                ('Phone_Number', models.IntegerField()),
                ('Password', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Authority_reg',
            },
        ),
        migrations.CreateModel(
            name='Offline_Booking',
            fields=[
                ('Customer_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Check_in', models.CharField(max_length=255)),
                ('Check_out', models.CharField(max_length=255)),
                ('First_Name', models.CharField(max_length=255)),
                ('Last_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Mobile_Number', models.IntegerField()),
                ('ADULT', models.CharField(max_length=255)),
                ('CHILDREN', models.CharField(max_length=255)),
                ('Total_Person', models.IntegerField()),
                ('Select_Room', models.CharField(max_length=255)),
                ('Room_Number', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('Personal_Identity', models.CharField(max_length=255)),
                ('Upload_Image', models.ImageField(upload_to='')),
                ('Country', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Offline_Booking_Customer',
            },
        ),
        migrations.CreateModel(
            name='Online_Booking',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Check_in', models.CharField(max_length=255)),
                ('Check_out', models.CharField(max_length=255)),
                ('ADULT', models.CharField(max_length=255)),
                ('CHILDREN', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Surname', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Phone_Number', models.IntegerField()),
                ('City', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('Nid_No', models.CharField(max_length=255)),
                ('Img', models.ImageField(upload_to='')),
                ('Address', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Online_Booking_table',
            },
        ),
        migrations.CreateModel(
            name='Add_Salarys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=255)),
                ('Mobile_Number', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=500)),
                ('Departments', models.CharField(max_length=255)),
                ('Salary', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
                ('Employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApp.add_employee')),
            ],
            options={
                'db_table': 'Add_Employee_salarys',
            },
        ),
    ]