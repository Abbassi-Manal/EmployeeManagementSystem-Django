
from django.shortcuts import render , redirect
from .models import Employee , Payements 
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    Emps = Employee.objects.all()
    context = {
        'Emp' : Emps
    }
    print(context)
    return render(request , 'index.html' , context)


def payments(request):
    Pay = Payements.objects.all()
    
    context = {
        'Pay' : Pay
    }
    return render(request , 'payments.html' , context)




def actions_employee(request):
    # print(' hello')
    if request.method == 'POST':
        matricule = request.POST['matricule']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = float(request.POST['salary'])
        new_emp = Employee(matricule=matricule, first_name=first_name, last_name=last_name, salary=salary)
        new_emp.save()
        # messages.success(request, 'Employee ajouté avec succès.')
        return redirect('index')  
    elif request.method == 'GET':
        return render(request, 'actions_employee.html')
    else:
        return HttpResponse("Invalid request method")


def actions_payments(request):
    if request.method == 'POST':
        matricule_str = request.POST.get('matricule')
        date_str = request.POST['date']
        amount = float(request.POST['amount'])
        employee = Employee.objects.get(matricule__iexact=matricule_str.strip())

        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        new_pay= Payements(matricule=employee, date=date, amount = amount)
        new_pay.save()
        # messages.success(request, 'Employee ajouté avec succès.')
        return redirect('payments')  
    elif request.method == 'GET':
        emp = Employee.objects.all()
        context = {
        'emps': emp  
        }
        print(context)
        return render(request, 'actions_payments.html', context)
    else:
        return HttpResponse("Invalid request method")

def history(request):
    if request.method == 'POST':
        date_str = request.POST.get("date")
        matricule_str = request.POST.get("matricule")

        if date_str or matricule_str:
            # Case: Either date or matricule provided
            Pay = Payements.objects.all()

            if date_str:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                Pay = Pay.filter(date=date)

            if matricule_str:
                try:
                    employee = Employee.objects.get(matricule=matricule_str)
                    Pay = Pay.filter(matricule=employee)
                except Employee.DoesNotExist:
                    messages.error(request, f"Employee with matricule {matricule_str} does not exist.")

            context = {'Pay': Pay}
            return render(request, 'history.html', context)
        else:
            error_message = "Invalid request. Please provide either date or matricule."
            messages.error(request, error_message)
            return redirect('history')

    elif request.method == 'GET':
        return render(request, 'history.html')



def delete_employee(request, matricule):
    if request.method == 'POST':
        try:
            employee = Employee.objects.get(matricule=matricule)
            employee.delete()
            messages.success(request, 'Employee deleted successfully.')
        except Employee.DoesNotExist:
            messages.error(request, f"Employee with matricule {matricule} does not exist.")

    return redirect('index')


def delete_payment(request, matricule):
    if request.method == 'POST':
        try:
            payments = Payements.objects.filter(matricule=matricule)
            if payments.exists():
                payments.delete()
                messages.success(request, 'payment deleted successfully.')
                return redirect('payments')
        except Employee.DoesNotExist:
            messages.error(request, f"payment for employee with matricule {matricule} does not exist.")

    return redirect('payments')