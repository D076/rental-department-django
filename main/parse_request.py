from .models import CleanWorker, AdminWorker, Apartment, CleanRequest, BronList


def get_employee(request):
    try:
        employee_type = None
        employee_id = None
        employee_name = None
        name = request.user.first_name
        if AdminWorker.objects.filter(admin_worker_name=name):
            employee_type = 'Администратор'
            employee = AdminWorker.objects.filter(admin_worker_name=name).first()
            employee_id, employee_name = str(employee).split('. ')

        if CleanWorker.objects.filter(clean_worker_name=name):
            employee_type = 'Уборщик'
            employee = CleanWorker.objects.filter(clean_worker_name=name).first()
            employee_id, employee_name = str(employee).split('. ')

        return employee_type, employee_id, employee_name
    except TypeError:
        return {}
