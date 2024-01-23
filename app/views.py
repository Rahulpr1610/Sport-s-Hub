from django.shortcuts import render,redirect
from app.models import tbl_equipment,tbl_managers,tbl_equipmentbooking,tbl_sales,tbl_user,tbl_turff,tbl_truff_booking,tbl_payment,login_tb
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
import os

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def user_home(request):
    return render(request,'user_home.html')

def manager_home(request):
    return render(request,'manager_home.html')

def sales_home(request):
    return render(request,'sales_home.html')

def user_register(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['pswd']
        c=request.POST['fname']
        d=request.POST['lname']
        e=request.POST['place']
        f=request.POST['phone']
        g=request.POST['email']
        l = login_tb(username=a, password=f, user_type='user')
        l.save()
        h=tbl_user(login_id=l,username=a,password=b,firstname=c,lastname=d,place=e,phone=f,email=g)
        i=User(username=a,first_name=c,last_name=d,email=g)
        i.set_password(b)
        i.save()
        h.save()
        return HttpResponse('<script>alert("Successfully Regist"),window.location="/#";</script>')
    return render(request,'user_register.html')
def manager_register(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['fname']
        c=request.POST['lname']
        d=request.POST['place']
        e=request.POST['email']
        f=request.POST['pswd']
        l=login_tb(username=a,password=f,user_type='manager')
        l.save()
        g=tbl_managers(login_id=l,username=a,firstname=b,lastname=c,place=d,email=e,password=f)
        h=User(username=a)
        h.set_password(f)
        h.save()
        g.save()
        return HttpResponse('<script>alert("Successfully Regist"),window.location="/#";</script>')
    return render(request,'manager_register.html')

def sales_register(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['pswd']
        c=request.POST['name']
        d=request.POST['place']
        e=request.POST['phone']
        f=request.POST['email']
        l = login_tb(username=a,password=b,user_type='sales')
        l.save()
        g=tbl_sales(login_id=l,username=a,password=b,name=c,place=d,phone=e,email=f)
        u=User(username=a)
        u.set_password(b)
        u.save()
        g.save()
        return HttpResponse('<script>alert("Successfully Regist"),window.location="/#";</script>')
    return render(request,'sales_register.html')

def login(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['pswd']

        c = authenticate(username=a, password=b)

        request.session['user_id'] = a
        if c is not None and c.is_superuser==1:
            return render(request,'admin_home.html')
        elif c is not None :
            q = login_tb.objects.get(username=a)
            if  c.is_superuser==0 and q.user_type=='user':
                return render(request,'user_home.html')
            
            elif c is not None and q.user_type=='manager':
                return render(request,'manager_home.html')
            elif c is not None and q.user_type=='sales':
                return render(request,'sales_home.html')
    return render(request,'login.html') 

def sales_login(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['paswd']
        c=authenticate(username=a,password=b)
        request.session['user_id'] = a
        if c is not None and c.is_superuser==0:
            return render(request,'sales_home.html')
    return render(request,'sales_login.html')
        


def logout(request):
    django_logout(request)
    return redirect('/home/')

def logout1(request):
    django_logout(request)
    return redirect('/manager_home/')

def logout2(request):
    django_logout(request)
    return redirect('/user_home/')

def salesaddeqp(request):
    sid=request.session['user_id']
    if request.method=='POST':
        b=request.POST['eqname']
        c=request.POST['qnty']
        d=request.POST['price']
        e=request.FILES['photo']
        f=tbl_equipment(sales_id=sid,equipment_name=b,quantity=c,price=d,photo=e)
        f.save()
        return HttpResponse('<script>alert("Successfully Regist"),window.location="/sales_home";</script>')
    return render(request,'sales_addeqp.html')

def view_eqp(request):
    a=tbl_equipment.objects.all()
    return render(request,'view_eqp.html',{'k':a})

def delete(request,id):
    a=tbl_equipment.objects.get(id=id)
    a.delete()
    return HttpResponse('<script>alert("success"),window.location="/view_eqp";</script>')

def update(request,id):
    a=tbl_equipment.objects.get(id=id)
    if request.method=='POST':
        a.sales_id=request.POST['sid']
        a.equipment_name=request.POST['eqname']
        a.quantity=request.POST['qnty']
        if len(request.FILES)!=0:
            if len(a.photo)>0:
                os.remove(a.photo.path)
                a.photo=request.FILES['photo']
        a.price=request.POST['price']
        a.save()
        return HttpResponse('<script>alert("success"),window.location="/view_eqp";</script>')
    return render(request,'view_eqp.html',{'b':a})

def manager_addturff(request):
    if request.method=='POST':
        a=request.POST['tname']
        b=request.POST['place']
        c=request.POST['email']
        d=request.POST['phone']
        e=request.POST['price']
        f=request.FILES['photo']
        g=tbl_turff(truff_name=a,place=b,email=c,phone=d,price=e,photo=f)
        g.save()
        return HttpResponse('<script>alert("successfully registered"),window.location="/manager_home";</script>')
    return render(request,'manager_addturff.html')

def view_turff(request):
    b=tbl_turff.objects.all()
    return render(request,'view_turff.html',{'d':b})

def delete_turff(request,id):
    b=tbl_turff.objects.get(id=id)
    b.delete()
    return HttpResponse('<script>alert("success"),window.location="/view_turff";</script>')

def update_turff(request,id):
    b=tbl_turff.objects.get(id=id)
    if request.method=='POST':
        b.truff_name=request.POST['tname']
        b.place=request.POST['place']
        b.email=request.POST['email']
        b.phone=request.POST['phone']
        b.price=request.POST['price']
        if len(request.FILES)!=0:
            if len(b.photo)>0:
                os.remove(b.photo.path)
            b.photo=request.FILES['photo']
        b.save()
        return HttpResponse('<script>alert("success"),window.location="/view_turff";</script>')
    return render(request,'view_turff.html',{'c':b})

def view_equipment(request):
    if request.method=='POST':
        a=request.POST['sid']
        b=request.POST['eqname']
        c=request.POST['qnty']
        d=request.POST['price']
        e=request.FILES['photo']
        f=tbl_equipment(sales_id=a,equipment_name=b,quantity=c,price=d,photo=e)
        f.save()
    return render(request,'user_view.html')


def view_equipment(request):
    a=tbl_equipment.objects.all()
    return render(request,'view_equipment.html',{'x':a})

def userview_turff(request):
    a=tbl_turff.objects.all()
    return render(request,'userview_turff.html',{'d':a})

def manager_viewbooking(request):
    a=tbl_truff_booking.objects.all()
    return render(request,'booking.html',{'f',a})

def quantity(request,id,pr,ename):
    uid=request.session['user_id']
    eq_id=id
    price=pr
    eq_name=ename
    if request.method=='POST':
        a=request.POST['qnty']
        total=int(a)*int(price)
        q=tbl_equipmentbooking(user_id=uid,equipment_id=eq_id,equipment_name=eq_name,quantity=a,total=total,status="pending")
        q.save()
        return HttpResponse('<script>alert("Order placed"),window.location="/view_equipment";</script>')
    return render(request,'quantity.html',{'p':price})

def booking(request):
    a=tbl_truff_booking.objects.all()
    return render(request,'booking.html',{'d':a})


def book_turff(request,id,pr,tname):
    uid=request.session['user_id']
    print(uid)
    tid=id
    tname=tname
    amt=pr
    q=tbl_truff_booking(user_id=uid,truff_id=tid,truff_name=tname,booking_amount=amt,status="pending")
    q.save()
    return HttpResponse('<script>alert("success"),window.location="/userview_turff";</script>')

def viewbooking(request):
    a=tbl_truff_booking.objects.all()
    return render(request,'manager_viewbooking.html',{'f':a})

def salesapprove(request,id):
    id=id
    a=tbl_equipmentbooking.objects.get(id=id)
    a.status="Approved"
    a.save()
    return HttpResponse('<script>alert("approved"),window.location="/view_eqp";</script>')


def salesreject(request,id):
    id=id
    a=tbl_equipmentbooking.objects.get(id=id)
    a.status="Reject"
    a.save() 
    return HttpResponse('<script>alert("rejected"),window.location="/sales_home";</script>')

def approve(request,id):
    id=id
    a=tbl_truff_booking.objects.get(id=id)
    a.status="Approved"
    a.save()
    return HttpResponse('<script>alert("approved"),window.location="/manager_viewbooking";</script>')

def reject(request,id):
    id=id
    a=tbl_truff_booking.objects.get(id=id)
    a.status="reject"
    a.save()
    return HttpResponse('<script>alert("rejected"),window.location="/manager_viewbooking";</script>')

def user_view_turff_booking(request):
    uid=request.session['user_id']
    q=tbl_truff_booking.objects.filter(user_id=uid)
    return render(request,'userbooking.html',{'b':q})

def vieworder(request):
    return render(request,'vieworder.html')

def viewturff_order(request):
    uid=request.session['user_id']
    a=tbl_truff_booking.objects.filter(user_id=uid)
    return render(request,'viewturff_order.html',{'b':a})



    
def turff_payment(request,id,bamount):
    uid=request.session['user_id']
    amt=bamount
    bkid=id
    q=tbl_truff_booking.objects.get(id=bkid)
    if request.method=='POST':
            a=tbl_payment(booking_id=id,user_id=uid,amount=amt)
            a.save()
            q.status="Paid"
            q.save()
            return HttpResponse('<script>alert("Payment Success"),window.location="/viewturfforder";</script>')
    return render(request,'makepayment.html',{'a':amt})

def vieweqp_order(request):
    uid=request.session['user_id']
    a=tbl_equipmentbooking.objects.filter(user_id=uid)
    return render(request,'viewepqorder.html',{'g':a})

def sales_viewbooking(request,id):
    eq_id=id
    q=tbl_equipment.objects.get(id=eq_id)
    eq_name=q.equipment_name
    print(eq_name)
    a=tbl_equipmentbooking.objects.filter(equipment_id=eq_id)
    return render(request,'sales_viewbooking.html',{'k':a,'ename':eq_name})
    
def makepaymenteqp(request,id,total):
    uid=request.session['user_id']
    bkid=id
    total=total
    q=tbl_equipmentbooking.objects.get(id=bkid)
    if request.method=='POST':
        a=tbl_payment(booking_id=id,user_id=uid,amount=total)
        a.save()
        q.status="Paid"
        q.save()
        return HttpResponse('<script>alert("payment Success"),window.location="/vieweqporder";</script>')
    return render(request,'makepayment.html',{'a':total})

def adminview_turff(request):
    a=tbl_turff.objects.all()
    return render(request,'adminview_turff.html',{'d':a})

def adminview_eqp(request):
    a=tbl_equipment.objects.all()
    return render(request,'adminview_eqp.html',{'x':a})


def adminview_turfforder(request):
    a=tbl_truff_booking.objects.all()
    return render(request,'adminview_turfforder.html',{'b':a})

def adminview_eqporder(request):
    a=tbl_equipmentbooking.objects.all()
    return render(request,'adminview_eqporder.html',{'g':a})

def adminview_user(request):
    a=tbl_user.objects.all()
    return render(request,'adminview_user.html',{'g':a})

def adminview_manager(request):
    a=tbl_managers.objects.all()
    return render(request,'adminview_manager.html',{'g':a})

def adminview_sales(request):
    a=tbl_sales.objects.all()
    return render(request,'adminview_sales.html',{'d':a})

def adminview_user(request):
    a=tbl_user.objects.all()
    return render(request,'adminview_user.html',{'d':a})

def adminview_manager(request):
    a=tbl_user.objects.all()
    return render(request,'adminview_manager.html',{'d':a})

# def admin_profile(request):
#     return render(request,'admin_profile.html')