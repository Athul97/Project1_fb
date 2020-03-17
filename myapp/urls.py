from django.urls import path
from . import views

urlpatterns = [
    # path('index', views.fn_index1),
    # path('',views.fn_test),
    # path('getdata/',views.fn_getData),

    path('',views.fn_login),
    path('userData/',views.fn_userData),
    path('signup/', views.fn_signup),
    path('change/', views.fn_chpass),
    # path('changepass/', views.fn_change_pass),
    path('profile/', views.fn_editprofile),


    path('update/', views.fn_update),
    path('updatepassword/', views.fn_updatepass),
 
]
