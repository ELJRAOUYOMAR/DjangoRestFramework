from . import views
from django.urls import path 

urlpatterns=[
    #display data
    path('display_data',views.display_data,name='display_data'),
    #display data from flespi
    path('data_flespi', views.data_flespi, name='data_flespi'),
    # path('json_format',views.json_format,name='json_format')
    #1 no rest no model
    path('no_rest_no_model',views.no_rest_no_model,name='no_rest_no_model'),
    #2 no rest from model
    path('no_rest_from_model',views.no_rest_from_model,name='no_rest_no_model'),
    #3.1 FBV_list GET , POST
    path('FBV_list',views.FBV_list,name='FBV_list'),
    #
    path('fbv_list_just_json',views.fbv_list_just_json,name='fbv_list_just_json'),
    #3.2 FBV_pk GET , PUT , DELETE
    path('FBV_pk/<int:pk>',views.FBV_pk,name='FBV_pk'),
    
]