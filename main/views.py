from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import (AdminWorker, CleanRequest, Customer, Apartment, BronList,
                     CleanWorker, ResidDoc, UserExtent)
from .forms import (CustomerForm, ApartmentForm, CleanRequestForm,
                    BronListForm, ResidDocForm)
from .parse_request import get_employee
from django.http import HttpResponse, HttpResponseRedirect


def login_user(request):
    if request.method == 'GET':
        return render(request, 'main/log_in.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/log_in.html',
                          {'form': AuthenticationForm(), 'error': "Неверное имя или пароль"})
        else:
            login(request, user)
            return redirect('main:home')


@login_required()
def home(request):
    if request.method == 'GET':
        employee_type, employee_id, employee_name = get_employee(request)
        dictionary = {'employee_type': employee_type,
                      'employee_id': employee_id,
                      'employee_name': employee_name}
        if employee_type == 'Администратор':
            dictionary.update({'customers': Customer.objects.all()})

        return render(request, 'main/home.html', dictionary)
    elif request.method == 'POST':
        pass


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


def redir(request):
    if request.method == 'GET':
        return redirect('main:home')


@login_required()
def clients(request):
    if request.method == 'GET':
        employee_type, employee_id, employee_name = get_employee(request)
        dictionary = {'employee_type': employee_type,
                      'employee_id': employee_id,
                      'employee_name': employee_name}
        if employee_type == 'Администратор':
            dictionary.update({'customers': Customer.objects.all()})
        form = CustomerForm()
        dictionary.update({'form': form})
        return render(request, 'main/customers.html', dictionary)
    elif request.method == "POST":
        pass


@login_required()
def change_client(request, pk_customer):
    employee_type, employee_id, employee_name = get_employee(request)
    dictionary = {'employee_type': employee_type,
                  'employee_id': employee_id,
                  'employee_name': employee_name}
    if pk_customer:
        client_ = Customer.objects.get(id_customer=pk_customer)
        if request.method == 'GET':
            form = CustomerForm(instance=client_)
            dictionary.update({'form': form})
            return render(request, 'main/change_customer.html', dictionary)
        elif request.method == 'POST':
            if 'save-client' in request.POST:
                form = CustomerForm(request.POST, instance=client_)
                form.save()
                return redirect('main:customers')
    else:
        if request.method == 'GET':
            form = CustomerForm()
            dictionary.update({'form': form})
            return render(request, 'main/change_customer.html', dictionary)
        elif request.method == 'POST':
            if 'save-client' in request.POST:
                form = CustomerForm(request.POST)
                form.save()
                return redirect('main:customers')


@login_required
def new_client(request):
    if request.method == 'GET':
        return change_client(request, None)
    elif request.method == 'POST':
        return change_client(request, None)


@login_required
def apartments(request):
    if request.method == 'GET':
        employee_type, employee_id, employee_name = get_employee(request)
        dictionary = {'employee_type': employee_type,
                      'employee_id': employee_id,
                      'employee_name': employee_name}
        if employee_type == 'Администратор':
            dictionary.update({'apartments': Apartment.objects.all()})
        form = ApartmentForm()
        dictionary.update({'form': form})
        return render(request, 'main/apartments.html', dictionary)
    elif request.method == "POST":
        pass


@login_required()
def change_apartment(request, pk_apartment):
    employee_type, employee_id, employee_name = get_employee(request)
    dictionary = {'employee_type': employee_type,
                  'employee_id': employee_id,
                  'employee_name': employee_name}
    if pk_apartment:
        apartment_ = Apartment.objects.get(id_apartment=pk_apartment)
        if request.method == 'GET':
            form = ApartmentForm(instance=apartment_)
            dictionary.update({'form': form})
            return render(request, 'main/change_apartment.html', dictionary)
        elif request.method == 'POST':
            if 'save-apartment' in request.POST:
                form = ApartmentForm(request.POST, instance=apartment_)
                form.save()
                return redirect('main:apartments')
    else:
        if request.method == 'GET':
            form = ApartmentForm()
            dictionary.update({'form': form})
            return render(request, 'main/change_apartment.html', dictionary)
        elif request.method == 'POST':
            if 'save-apartment' in request.POST:
                form = ApartmentForm(request.POST)
                form.save()
                return redirect('main:apartments')


@login_required
def new_apartment(request):
    if request.method == 'GET':
        return change_apartment(request, None)
    elif request.method == 'POST':
        return change_apartment(request, None)


@login_required()
def clean_requests(request):
    if request.method == 'GET':
        employee_type, employee_id, employee_name = get_employee(request)
        dictionary = {'employee_type': employee_type,
                      'employee_id': employee_id,
                      'employee_name': employee_name}
        if employee_type == 'Администратор':
            dictionary.update({'clean_requests': CleanRequest.objects.all()})
        elif employee_type == 'Уборщик':
            dictionary.update({'clean_requests': CleanRequest.objects.filter(id_clean_worker=employee_id)})
        form = CleanRequestForm()
        dictionary.update({'form': form})
        return render(request, 'main/clean_requests.html', dictionary)
    elif request.method == "POST":
        pass


@login_required()
def change_clean_request(request, pk_clean_request):
    employee_type, employee_id, employee_name = get_employee(request)
    dictionary = {'employee_type': employee_type,
                  'employee_id': employee_id,
                  'employee_name': employee_name}
    if pk_clean_request:
        clean_request_ = CleanRequest.objects.get(id_clean_request=pk_clean_request)
        if request.method == 'GET':
            form = CleanRequestForm(instance=clean_request_)
            dictionary.update({'form': form})
            return render(request, 'main/change_clean_request.html', dictionary)
        elif request.method == 'POST':
            if 'save-clean-request' in request.POST:
                form = CleanRequestForm(request.POST, instance=clean_request_)
                form.save()
                return redirect('main:clean_requests')
            elif 'close-clean-request' in request.POST:
                pk_apartment = str(clean_request_.id_apartment)

                pk_apartment = pk_apartment[:12].split('.')[0]
                apartment_ = Apartment.objects.get(id_apartment=pk_apartment)
                apartment_.apartment_status = 'Готов'
                apartment_.save()

                clean_request_.delete()

                return redirect('main:clean_requests')
    else:
        if request.method == 'GET':
            form = CleanRequestForm()
            dictionary.update({'form': form})
            dictionary.update({'new': True})
            return render(request, 'main/change_clean_request.html', dictionary)
        elif request.method == 'POST':
            if 'save-clean-request' in request.POST:
                form = CleanRequestForm(request.POST)
                form.save()

                pk_apartment = str(form.cleaned_data.get('id_apartment'))
                pk_apartment = pk_apartment[:12].split('.')[0]
                apartment_ = Apartment.objects.get(id_apartment=pk_apartment)
                apartment_.apartment_status = 'Нуждается в уборке'
                apartment_.save()

                return redirect('main:clean_requests')


@login_required()
def new_clean_request(request):
    if request.method == 'GET':
        return change_clean_request(request, None)
    elif request.method == "POST":
        return change_clean_request(request, None)


@login_required()
def bron_lists(request):
    if request.method == 'GET':
        employee_type, employee_id, employee_name = get_employee(request)
        dictionary = {'employee_type': employee_type,
                      'employee_id': employee_id,
                      'employee_name': employee_name}
        if employee_type == 'Администратор':
            dictionary.update({'bron_lists': BronList.objects.all()})
        form = BronListForm()
        dictionary.update({'form': form})
        return render(request, 'main/bron_lists.html', dictionary)
    elif request.method == "POST":
        pass


@login_required()
def change_bron_list(request, pk_bron_list):
    employee_type, employee_id, employee_name = get_employee(request)
    dictionary = {'employee_type': employee_type,
                  'employee_id': employee_id,
                  'employee_name': employee_name}
    if pk_bron_list:
        bron_list_ = BronList.objects.get(id_bron_list=pk_bron_list)
        if request.method == 'GET':
            form = BronListForm(instance=bron_list_)
            dictionary.update({'form': form})
            return render(request, 'main/change_bron_list.html', dictionary)
        elif request.method == 'POST':
            if 'save-bron-list' in request.POST:
                form = BronListForm(request.POST, instance=bron_list_)
                form.save()
                return redirect('main:bron_lists')
            elif 'close-bron-list' in request.POST:
                pk_apartment = str(bron_list_.id_apartment)

                pk_apartment = pk_apartment.split('.')[0]
                apartment_ = Apartment.objects.get(id_apartment=pk_apartment)
                apartment_.apartment_status = 'Готов'
                apartment_.save()

                bron_list_.delete()

                return redirect('main:bron_lists')
    else:
        if request.method == 'GET':
            form = BronListForm()
            dictionary.update({'form': form})
            dictionary.update({'new': True})
            return render(request, 'main/change_bron_list.html', dictionary)
        elif request.method == 'POST':
            if 'save-bron-list' in request.POST:
                form = BronListForm(request.POST)
                form.save()

                pk_apartment = str(form.cleaned_data.get('id_apartment'))
                pk_apartment = pk_apartment.split('.')[0]
                apartment_ = Apartment.objects.get(id_apartment=pk_apartment)
                apartment_.apartment_status = 'Забронировано'
                apartment_.save()

                return redirect('main:bron_lists')


@login_required()
def new_bron_list(request):
    if request.method == 'GET':
        return change_bron_list(request, None)
    elif request.method == "POST":
        return change_bron_list(request, None)


@login_required()
def resid_docs(request):
    if request.method == 'GET':
        employee_type, employee_id, employee_name = get_employee(request)
        dictionary = {'employee_type': employee_type,
                      'employee_id': employee_id,
                      'employee_name': employee_name}
        if employee_type == 'Администратор':
            dictionary.update({'resid_docs': ResidDoc.objects.all()})
        form = ResidDocForm()
        dictionary.update({'form': form})
        return render(request, 'main/resid_docs.html', dictionary)
    elif request.method == "POST":
        pass


@login_required()
def change_resid_doc(request, pk_resid_doc):
    employee_type, employee_id, employee_name = get_employee(request)
    dictionary = {'employee_type': employee_type,
                  'employee_id': employee_id,
                  'employee_name': employee_name}
    if pk_resid_doc:
        resid_doc_ = ResidDoc.objects.get(id_doc=pk_resid_doc)
        if request.method == 'GET':
            form = ResidDocForm(instance=resid_doc_)
            dictionary.update({'form': form})
            return render(request, 'main/change_resid_doc.html', dictionary)
        elif request.method == 'POST':
            if 'save-resid-doc' in request.POST:
                form = ResidDocForm(request.POST, instance=resid_doc_)
                form.save()
                return redirect('main:resid_docs')
            elif 'close-resid-doc' in request.POST:
                pk_apartment = str(resid_doc_.id_apartment)
                resid_doc_.delete()

                return redirect('main:resid_docs')
    else:
        if request.method == 'GET':
            form = ResidDocForm()
            dictionary.update({'form': form})
            dictionary.update({'new': True})
            return render(request, 'main/change_resid_doc.html', dictionary)
        elif request.method == 'POST':
            if 'save-resid-doc' in request.POST:
                form = ResidDocForm(request.POST)
                form.save()
                return redirect('main:resid_docs')


@login_required()
def new_resid_doc(request):
    if request.method == 'GET':
        return change_resid_doc(request, None)
    elif request.method == "POST":
        return change_resid_doc(request, None)

