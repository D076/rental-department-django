from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('customers', views.clients, name='customers'),
    path('customer/<int:pk_customer>', views.change_client, name='change_customer'),
    path('customer/new', views.new_client, name='new_customer'),
    path('apartments', views.apartments, name='apartments'),
    path('apartment/<int:pk_apartment>', views.change_apartment, name='change_apartment'),
    path('apartment/new', views.new_apartment, name='new_apartment'),
    path('clean_requests', views.clean_requests, name='clean_requests'),
    path('clean_request/<int:pk_clean_request>', views.change_clean_request, name='change_clean_request'),
    path('clean_request/new', views.new_clean_request, name='new_clean_request'),
    path('bron_lists', views.bron_lists, name='bron_lists'),
    path('bron_list/<int:pk_bron_list>', views.change_bron_list, name='change_bron_list'),
    path('bron_list/new', views.new_bron_list, name='new_bron_list'),
    path('resid_docs', views.resid_docs, name='resid_docs'),
    path('resid_doc/<int:pk_resid_doc>', views.change_resid_doc, name='change_resid_doc'),
    path('resid_doc/new', views.new_resid_doc, name='new_resid_doc'),
]