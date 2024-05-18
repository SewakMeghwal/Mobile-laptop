"""web_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from web_app import views

admin.site.site_header = "Mobile Shop Admin"
admin.site.site_title = "Mobile Shop Admin Portal"
admin.site.index_title = "Welcome to Mobile Shop"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('bhome',views.bhome,name='bhome'),
    path('about',views.about,name='about'),
    path('mobile',views.mobiles,name='mobile'),
    path('laptop',views.laptops,name='laptop'),
    path('accessories',views.accessoriess,name='accessrioes'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('contects',views.cshow,name='contects'),
    path('contectf',views.cform,name='contectf'),
    path('profiles',views.pshow,name='profiles'),
    path('profilef',views.pform,name='profilef'),
    path('deletei<int:id>',views.deletei,name='deletei'),
    path('updatei<int:id>',views.updatei,name='updatei'),
    path('aform',views.adda,name='aform'),
    path('search',views.search,name='search'),
    path('madd',views.addm,name='madd'),
    path('ladd',views.addl,name='ladd'),
    path('aadd',views.adda,name='aadd'),
    path('aread <int:id>',views.areadmore,name='aread'),
    path('mread <int:id>',views.mreadmore,name='mread'),
    path('lread <int:id>',views.lreadmore,name='lread'),
    path('not',views.Not,name='not'),
    path('cart',views.cart,name='cart'),
    path('cart/add/<str:item_type>/<int:item_id>',views.cart_add,name='cart_add'),
    path('cart/remove/<str:item_type>/<int:item_id>',views.cart_remove,name='cart_remove'),
    path('cart/buy',views.cart_buy,name='cart_buy'),
   

]
