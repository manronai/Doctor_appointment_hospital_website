from django.shortcuts import render, redirect
from .forms import PatientUpdateForm, DoctorUpdateForm, CategoryForm
from .models import Doctor, Patient
# Create your views here.

def home(request):


    return render(request, 'users/home.html')

def category(request):

    if request.method== 'POST':  #usring redirect and session to send data to another function
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['cat'] = cd.get('name')
        return redirect('doctordetails')
    else:
        form = CategoryForm()
    return render(request, 'users/category.html', {'form': form})

def update(request):
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DoctorUpdateForm()
    return render(request, 'users/update.html', {'form': form})

def doctordetails(request):
    if request.method== 'POST': # action url name to send form data to this function url
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['cat'] = cd.get('name')
    temp = 0
    if request.session['cat'] == 'Obstetricians and gynecologists':
        temp = 'Obstetricians and gynecologists'
    elif request.session['cat'] == 'Psychiatrists':
        temp = 'Psychiatrists'
    elif request.session['cat'] == 'Neurologists':
        temp = 'Neurologists'
    elif request.session['cat'] == 'Cardiologists':
        temp = 'Cardiologists'
    else:
        context = {
            'pst': Doctor.objects.all()
        }
    if temp:
        context = {
            'pst': Doctor.objects.filter(category=temp)
        }

    return render(request, 'users/doctordetails.html', context)
drName = 'Dr. A'
def patientdetails(request):
    global drName
    if 'your_name' in request.POST.keys():
        drName = request.POST['your_name']
        form = PatientUpdateForm()
    else:
        if request.method == 'POST':
            form = PatientUpdateForm(request.POST)
            if form.is_valid():
                print(request.POST)

                dr = Doctor.objects.get(name=drName)

                dr.dailyoccupation += 1
                dr.save()
                ins = form.save(commit=False)
                ins.save()
                ins.doctors.add(dr)
                ins.serial = dr.dailyoccupation
                instance = form.save(commit=False)
                instance.age = 2022-int(instance.dob.split("-")[0])
                instance.save()
        else:
            form = PatientUpdateForm()

    form= PatientUpdateForm()


    return render(request, 'users/patientdetails.html', { 'form':form})
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin')
def allpatients(request):


    context = {
        'pst': Patient.objects.all()
    }
    return render(request, 'users/allpatients.html', context)

def deletePatient(request):
    global drName
    if 'your_name' in request.POST.keys():
        drName = request.POST['your_name']
        Patient.objects.filter(phone=drName).delete()

        return redirect('allpatients')
    return redirect('allpatients')

def contact(request):
    return render(request, 'users/contact.html')

def about(request):
    return render(request, 'users/about.html')
