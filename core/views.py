from django.shortcuts import render, redirect, HttpResponse
from core.models import *
# Create your views here.
def people_view(request):
    people = Person.objects.all()
    return render(request, 'list.html', {'people': people})

def new_person(request):
    if request.method == 'GET':
        return render(request, 'formularz.html')

    elif request.method == 'POST':
        phone_number = request.POST.get('phone')
        phone_type = request.POST.get('phone_type')
        email_adress = request.POST.get('email')
        email_type = request.POST.get('email_type')
        phone = Phone.objects.create(phone_number=phone_number, phone_type=phone_type)
        email = Email.objects.create(email=email_adress, email_type=email_type)
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        Person.objects.create\
            (name=name, surname=surname, somebodys_phone=phone, somebodys_emails=email)
        return redirect('list')

def modify(request, id):
    person = Person.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'modify.html', {'person': person})
    elif request.method == 'POST':
        phone_number = request.POST.get('phone')
        phone_type = request.POST.get('phone_type')
        email_adress = request.POST.get('email')
        email_type = request.POST.get('email_type')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        person.name = name
        person.surname = surname
        person.save()
        if person.somebodys_phone is not None:
            if phone_number or phone_type:
                pass
#                 NADPISZ DANE W INSTNIEJĄCYM OBIEKCIE
            else:
               pass
#                 skasuj obiekt
        else:
            if phone_number or phone_type:
                pass
#             create objects
            else:
                pass
#             do nothing

def show(request, id):
    person = Person.objects.get(id=id)
    name = person.name
    surname = person.surname
    text = name + " " + surname
    return HttpResponse(text)


def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    text = "skasowano osobę"
    return HttpResponse(text)




