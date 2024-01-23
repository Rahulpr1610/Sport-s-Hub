from django.db import models

# Create your models here.

class login_tb(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100)
class tbl_managers(models.Model):
    login_id=models.ForeignKey(login_tb,on_delete=models.CASCADE,default=1)
    username=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    class meta:
        db_tabel="tbl_managers"   

class tbl_sales(models.Model):
    login_id = models.ForeignKey(login_tb, on_delete=models.CASCADE, default=1)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=20)
    phone=models.IntegerField()        
    email=models.CharField(max_length=30)
    class meta:
        db_sales="tbl_sales"

class tbl_equipment(models.Model):
    sales_id=models.CharField(max_length=30)
    equipment_name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    photo=models.FileField(null=True)
    price=models.CharField(max_length=10)
    class meta:
        db_equipment="tbl_equipment"

class tbl_equipmentbooking(models.Model):
    user_id=models.CharField(max_length=10)
    equipment_id=models.IntegerField()
    equipment_name=models.CharField(max_length=10)
    quantity=models.CharField(max_length=10)
    total=models.CharField(max_length=10)
    status=models.CharField(max_length=100)
    class meta:
        db_equipmentbooking="tbl_equipmentbooking"

class tbl_user(models.Model):
    login_id = models.ForeignKey(login_tb, on_delete=models.CASCADE, default=1)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    class meta:
        db_user="tbl_user"

class tbl_turff(models.Model):
    truff_name=models.CharField(max_length=30)
    place=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    photo=models.FileField(null=True)
    class meta:
        db_truff="tbl_truff"


class tbl_truff_booking(models.Model):
    user_id=models.CharField(max_length=100)
    truff_id=models.CharField(max_length=10)
    truff_name=models.CharField(max_length=30)
    booking_amount=models.CharField(max_length=20)
    status=models.CharField(max_length=100)
    class meta:
        db_truff_booking="tbl_truff_booking"



class tbl_payment(models.Model):
    booking_id=models.CharField(max_length=20)
    user_id=models.CharField(max_length=10)
    amount=models.CharField(max_length=20)
    class meta:
        db_payment="tbl_payment"
    

