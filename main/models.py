from django.db import models
from django.contrib.auth.models import User


class UserExtent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_extent = models.CharField(max_length=20)


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_pasport = models.CharField(max_length=20)
    id_customer = models.AutoField(db_column='id_customer', primary_key=True)

    def __str__(self):
        return f'{self.customer_name} | {self.customer_pasport}'

    class Meta:
        managed = False
        db_table = 'customer'


class AdminWorker(models.Model):
    admin_worker_name = models.CharField(max_length=100)
    id_admin_worker = models.AutoField(db_column='id_admin_worker', primary_key=True)

    def __str__(self):
        return f'{self.id_admin_worker}. {self.admin_worker_name}'

    class Meta:
        managed = True
        db_table = 'admin_worker'


class CleanWorker(models.Model):
    clean_worker_name = models.CharField(max_length=100)
    id_clean_worker = models.AutoField(db_column='id_clean_worker', primary_key=True)

    def __str__(self):
        return f'{self.id_clean_worker}. {self.clean_worker_name}'

    class Meta:
        managed = True
        db_table = 'clean_worker'


class Apartment(models.Model):
    apartment_rooms = models.IntegerField()
    apartment_price = models.IntegerField()
    apartment_status = models.CharField(max_length=50)
    id_apartment = models.AutoField(db_column='id_apartment', primary_key=True)

    def __str__(self):
        return f'{self.id_apartment}. Кол-во комнат: {self.apartment_rooms}, ' \
               f'цена: {self.apartment_price}, статус: {self.apartment_status}'

    class Meta:
        managed = False
        db_table = 'apartment'


class CleanRequest(models.Model):
    clean_request_date = models.DateField()
    id_clean_request = models.AutoField(db_column='id_clean_request', primary_key=True)
    id_clean_worker = models.ForeignKey(CleanWorker, models.DO_NOTHING, db_column='id_clean_worker')
    id_admin_worker = models.ForeignKey(AdminWorker, models.DO_NOTHING, db_column='id_admin_worker')
    id_apartment = models.ForeignKey(Apartment, models.DO_NOTHING, db_column='id_apartment')

    def __str__(self):
        return f"""Дата: {self.clean_request_date.strftime('%d.%m.%Y')}\n
Квартира: {self.id_apartment}\n
Уборщик: {self.id_clean_worker}\n
Администратор: {self.id_admin_worker}"""

    class Meta:
        managed = False
        db_table = 'clean_request'


class BronList(models.Model):
    bron_number = models.CharField(max_length=20, blank=True, null=True)
    id_bron_list = models.AutoField(db_column='id_bron_list', primary_key=True)
    id_admin_worker = models.ForeignKey(AdminWorker, models.DO_NOTHING, db_column='id_admin_worker')
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    id_apartment = models.ForeignKey(Apartment, models.DO_NOTHING, db_column='id_apartment')

    def __str__(self):
        return f"""№: {self.bron_number}\n
Клиент: {self.id_customer}\n
Квартира: {self.id_apartment}\n
Администратор: {self.id_admin_worker}"""

    class Meta:
        managed = False
        db_table = 'bron_list'


class ResidDoc(models.Model):
    doc_date_start = models.DateField()
    doc_date_end = models.DateField(blank=True, null=True)
    doc_price = models.IntegerField(blank=True, null=True)
    id_doc = models.AutoField(db_column='id_doc', primary_key=True)
    id_admin_worker = models.ForeignKey(AdminWorker, models.DO_NOTHING, db_column='id_admin_worker')
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    id_apartment = models.ForeignKey(Apartment, models.DO_NOTHING, db_column='id_apartment')

    def __str__(self):
        return f"""{self.id_doc}. Клиент: {self.id_customer}\n
Квартира: {self.id_apartment}\n
Дата заселения: {self.doc_date_start.strftime('%d.%m.%Y')}\n
Дата выселения: {self.doc_date_end.strftime('%d.%m.%Y')}\n
Администратор: {self.id_admin_worker}"""

    class Meta:
        managed = False
        db_table = 'resid_doc'
