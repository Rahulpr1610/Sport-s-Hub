"""
URL configuration for sportshub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home),
    path('',views.index),
    # path('index/',views.index),
    path('home/',views.home),
    path('login/',views.login),
    path('logout/',views.logout),
    path('logout1/',views.logout1),
    path('logoutuser/',views.logout2),
    # path('cart/',views.cart),
    path('user_home/',views.user_home),
    path('manager_home/',views.manager_home),
    path('manager_register/',views.manager_register),
    path('user_register/',views.user_register),
    path('sales_register/',views.sales_register),
    path('sales_home/',views.sales_home),
    path('sales_addeqp/',views.salesaddeqp),
    path('view_eqp/',views.view_eqp),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    # path('manager_home/',views.manager_home),
    path('manager_addturff/',views.manager_addturff),
    path('view_turff/',views.view_turff),
    path('delete_turff/<int:id>',views.delete_turff),
    path('update_turff/<int:id>',views.update_turff),
    # path('equipment_booking/',views.equipment_booking),
    path('view_equipment/',views.view_equipment),
    path('userview_turff/',views.userview_turff),
    path('quantity/',views.quantity),
    path('quantity/<int:id>/<pr>/<str:ename>',views.quantity),
    path('booking/<int:id>/<tname>/<pr>',views.book_turff),
    path('manager_viewbooking/',views.viewbooking),
    path('manager_viewbooking/',views.manager_viewbooking),
    path('sales_viewbooking/<int:id>',views.sales_viewbooking),
    path('salesapprove/<int:id>',views.salesapprove),
    path('salesreject/<int:id>',views.salesreject),
    path('approve/<int:id>',views.approve),
    path('reject/<int:id>',views.reject),
    path('userbooking/',views.user_view_turff_booking),
    path('vieworder/',views.vieworder),
    path('viewturfforder/',views.viewturff_order),
    path('vieweqporder/',views.vieweqp_order),
    path('turff_payment/<int:id>/<int:bamount>',views.turff_payment),
    path('makepaymenteqp/<int:id>/<int:total>',views.makepaymenteqp),
    path('sales_login/',views.sales_login),
    path('adminview_turff/',views.adminview_turff),
    path('adminview_eqp/',views.adminview_eqp),
    path('adminview_turfforder/',views.adminview_turfforder),
    path('adminview_eqporder/',views.adminview_eqporder),
    path('adminview_user/',views.adminview_user),
    path('adminview_manager/',views.adminview_manager),
    path('adminview_sales/',views.adminview_sales),
    # path('admin_profile/',views.admin_profile),
]  

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)
