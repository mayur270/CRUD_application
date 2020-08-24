from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
##########################################################
from .models import EmployeeModel
from .forms import EmployeeForm
##########################################################

@login_required
def home(request):
    employees = EmployeeModel.objects.all()
    return render(request, 'home.html', {'employees': employees})

def saving_employee_details(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            employees = EmployeeModel.objects.all()
            data['employee_list'] = render_to_string('includes/list_employees.html', {
                'employees': employees
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['employee_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def create_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
    return saving_employee_details(request, form, 'includes/create_employees.html')

@login_required
def update_view(request, pk):
    employee = get_object_or_404(EmployeeModel, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return saving_employee_details(request, form, 'includes/update_employees.html')

@login_required
def delete_view(request, pk):
    employee = get_object_or_404(EmployeeModel, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = EmployeeModel.objects.all()
        data['employee_list'] = render_to_string('includes/list_employees.html', {
            'employees': employees
        })
    else:
        context = {'employee': employee}
        data['employee_form'] = render_to_string('includes/delete_employees.html',
            context,
            request=request,
        )
    return JsonResponse(data)
