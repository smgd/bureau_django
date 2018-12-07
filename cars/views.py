from django.shortcuts import render, HttpResponse

from cars.forms import CarForm, PeriodForm
from cars.models import Car

def home(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return HttpResponse('good')
    else:
        form = CarForm()
        context = {'form': form}

    return render(request, 'cars/index.html', context)

def list(request):
    print(Car.objects.all())
    context = {'cars': Car.objects.all()}
    return render(request, 'cars/list.html', context)



def period(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)

        if form.is_valid():
            start_of_period = form.cleaned_data['start_of_period'] 
            end_of_period = form.cleaned_data['end_of_period']

            if start_of_period <= end_of_period:
                cars = (
                    Car.objects
                    .exclude(creation_date__gt=end_of_period)
                    .exclude(disposal_date__lt=start_of_period)
                )

                if len(cars) > 0:
                    context = {'cars': cars}
                    
                    return render(request, 'cars/list.html', context)
                else:
                    return HttpResponse('no cars in this period')
            else:
                return HttpResponse('period is not valid')
        else:
            return HttpResponse('form is not valid')
    else:
        form = PeriodForm()
        context = {'form': form}
        return render(request, 'cars/period.html', context)
