"""final_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.urls.conf import re_path
# from django.views.static import serve 
from django.urls import path
from final_app import views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from final_app.views import Index, Cart, CheckOut, OrderView, Products, Search
from final_app.middlewares.auth import auth_middleware
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
 
    path('password_reset/',auth_views.PasswordResetView. as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
  

    path('base/', views.base, name="base"),
    # path('', views.index, name="index"),
    path('', Index.as_view(), name="index"),
    path('products/', Products.as_view(), name="products"),
    path('search/', Search.as_view(), name="search"),
    path('cart/', Cart.as_view(), name="cart"),
    path('checkout/', CheckOut.as_view(), name="checkout"),
    path('orders/', auth_middleware(OrderView.as_view()), name="orders"),
    # path('checkout/', auth_middleware(CheckView.as_view()), name="checkout"),
    path('services/', views.services, name="services"),
    path('developers-section/', views.developers, name="developers-section"),
    path('disclaimer/', views.disclaimer, name="disclaimer"),
    path('privacy/', views.privacy, name="privacy"),
    path('terms/', views.terms, name="terms"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('cartlogin/', auth_middleware(views.cartlogin), name="cartlogin"),
    # path('user_action/', views.user_actions, name="user_actions"),
    path('user_dashboard', views.user_dashboard, name="user_dashboard"),
    # path('changepass', views.changepass, name="changepass"),
    path('logout/', views.logout, name="logout"),
    path('prodform/', views.prodform, name="Insert"),
    

    path('product-details/<int:id>/', views.product_details, name="product-details"),
    # path('products/', views.products, name="products"),

    path('submit_contact/', views.submit_contact, name="submit_contact"),
    path('delete_feedback/<int:id>/',views.delete_feedback,name="delete_feedback"),
    path('submit_appointment/', views.submit_appointment, name="submit_appointment"),
    path('donate/', views.donate, name="donate"),
    path('delete_donate/<int:id>/',views.delete_donate,name="delete_donate"),

    path('admin_register/', views.admin_register, name="admin_register"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),

    path('doctor_register/', views.doctor_register, name="doctor_register"),
    path('doctor_login/', views.doctor_login, name="doctor_login"),
    path('doctor_logout/', views.doctor_logout, name="doctor_logout"),
    path('doctor_dashboard/', views.doctor_dashboard, name="doctor_dashboard"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    # path('make_appointment/', views.make_appointment, name="make_appointment"),

    # path('search/', views.search, name='search'),

    path('404/', views.error_404, name='404'),
    path('500/', views.error_500, name='500'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

