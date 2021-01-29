from django.forms import ModelForm, DateField, SelectDateWidget, ModelChoiceField, Form
from .models import (CleanRequest, Customer, Apartment, BronList, ResidDoc, CleanWorker, AdminWorker)
from datetime import datetime


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_phone', 'customer_pasport']
        labels = {'customer_name': 'ФИО',
                  'customer_phone': 'Телефон',
                  'customer_pasport': 'Пасспортные данные'}


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['apartment_rooms', 'apartment_price', 'apartment_status']
        labels = {'apartment_rooms': 'Количество комнат',
                  'apartment_price': 'Цена за сутки',
                  'apartment_status': 'Статус'}


class CleanRequestForm(ModelForm):
    START_DATE = 2000
    clean_request_date = DateField(
        widget=SelectDateWidget(years=[i for i in range(START_DATE, int(datetime.today().year) + 1)]),
        label='Дата запроса',
        initial=datetime.today()
    )
    id_apartment = ModelChoiceField(queryset=Apartment.objects.all(), empty_label=None, label='Апартаменты')
    id_clean_worker = ModelChoiceField(queryset=CleanWorker.objects.all(), empty_label=None, label='Уборщик')
    id_admin_worker = ModelChoiceField(queryset=AdminWorker.objects.all(), empty_label=None, label='Администратор')

    class Meta:
        model = CleanRequest

        fields = ['clean_request_date', 'id_apartment', 'id_clean_worker',  'id_admin_worker']
        labels = {'clean_request_date': 'Дата запроса',
                  'id_apartment': 'Апартаменты',
                  'id_clean_worker': 'Уборщик',
                  'id_admin_worker': 'Администратор'}


class BronListForm(ModelForm):
    id_customer = ModelChoiceField(queryset=Customer.objects.all(), empty_label=None, label='Клиент')
    id_apartment = ModelChoiceField(queryset=Apartment.objects.all(), empty_label=None, label='Апартаменты')
    id_admin_worker = ModelChoiceField(queryset=AdminWorker.objects.all(), empty_label=None, label='Администратор')

    class Meta:
        model = BronList

        fields = ['bron_number', 'id_customer', 'id_apartment', 'id_admin_worker']
        labels = {'bron_number': '№',
                  'id_customer': 'Клиент',
                  'id_apartment': 'Апартаменты',
                  'id_admin_worker': 'Администратор'}


class ResidDocForm(ModelForm):
    START_DATE = 2000
    doc_date_start = DateField(
        widget=SelectDateWidget(years=[i for i in range(START_DATE, int(datetime.today().year) + 1)]),
        label='Дата заселения',
    )
    doc_date_end = DateField(
        widget=SelectDateWidget(years=[i for i in range(START_DATE, int(datetime.today().year) + 1)]),
        label='Дата выселения',
        initial=datetime.today()
    )

    id_customer = ModelChoiceField(queryset=Customer.objects.all(), empty_label=None, label='Клиент')
    id_apartment = ModelChoiceField(queryset=Apartment.objects.all(), empty_label=None, label='Апартаменты')
    id_admin_worker = ModelChoiceField(queryset=AdminWorker.objects.all(), empty_label=None, label='Администратор')

    class Meta:
        model = ResidDoc

        fields = ['doc_date_start', 'doc_date_end', 'id_customer', 'id_apartment', 'doc_price', 'id_admin_worker']
        labels = {'doc_date_start': 'Дата заселения',
                  'doc_date_end': 'Дата выселения',
                  'id_customer': 'Клиент',
                  'id_apartment': 'Апартаменты',
                  'doc_price': 'Цена',
                  'id_admin_worker': 'Администратор'}
