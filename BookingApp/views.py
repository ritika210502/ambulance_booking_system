from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from BookingApp.models import user, hospital, ambulance, patient, hos_patient, av_hospital, av_ambulance, Emergency
from django.core.exceptions import ValidationError


# Create your views here.

def index(request):
    return render(request, 'index.html')


def userPage(request):
    return render(request, 'userPage.html')


def ambulancePage(request):
    return render(request, 'ambulancePage.html')


def hospitalPage(request):
    return render(request, 'hospitalPage.html')


def login(request):
    return render(request, 'login.html')


def signUp(request):
    return render(request, 'signUp.html')


def am_booking(request):
    return render(request, 'am_booking.html')


def emg_booking(request):
    return render(request, "emg_booking.html")


def search_hospital(request):
    return render(request, 'search_hospital.html')


def enter_city(request):
    return render(request, 'enter_city.html')


def avHospital(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phNo = request.POST['phNo']
        Street = request.POST['Street']
        City = request.POST['City']
        State = request.POST['State']
        Zip = request.POST['Zip']
        a = av_hospital(name=name, email=email, phNo=phNo, Street=Street, City=City,
                        State=State, Zip=Zip)
        a.save()

        return render(request, 'hos_bookingform.html')


def hos_bookingform(request):
    hospitals = hospital.objects.all()
    return render(request, 'hos_bookingform.html', {'hospitals': hospitals})


def signUp(request):
    if request.method == "POST":
        usertype = request.POST.get('usertype')
        name = request.POST['name']
        email = request.POST['email']
        request.session['email'] = email
        password = request.POST['password']
        request.session['email'] = email

        if (usertype == 'HOSPITAL'):
            person = hospital(usertype='HOSPITAL', name=name,
                              email=email, password=password)
            person.save()
            current_user = hospital.objects.get(email=email)

            context = {
                'current_user': current_user,
            }

            return render(request, 'hospitalPage.html', context)

        elif (usertype == 'AMBULANCE'):
            person = ambulance(usertype='AMBULANCE', name=name,
                               email=email, password=password)
            person.save()
            current_user = ambulance.objects.get(email=email)

            context = {
                'current_user': current_user,
            }
            return render(request, 'ambulancePage.html', context)

        elif (usertype == 'USER'):
            person = user(usertype='USER', name=name,
                          email=email, password=password)
            person.save()
            current_user = user.objects.get(email=email)
            context = {
                'current_user': current_user,
            }
            # request.session['email'] = email

            return render(request, 'userPage.html', context)

    return render(request, 'signUp.html')


def login(request):
    if request.method == "POST":
        usertype = request.POST.get('usertype')
        email = request.POST['email']
        request.session['email'] = email
        password = request.POST['password']
        request.session['email'] = email
        if usertype == "USER":
            nuser = user.objects.filter(email=email, password=password)
            if not nuser:
                messages.error(
                    request, 'username or password are invalid (:\n Please try again')
                return redirect('login')

            current_user = user.objects.get(email=email)
            av_ambulance1 = av_ambulance.objects.all()

            context = {
                'current_user': current_user,
                'hospitals':av_ambulance1,

            }
            
            return render(request, 'userPage.html',context)

        if usertype == "HOSPITAL":
            nuser = hospital.objects.filter(email=email, password=password)
            if not nuser:
                messages.error(
                    request, 'username or password are invalid (:\n Please try again')
                return redirect('login')

            current_user = hospital.objects.get(email=email)
            context = {
                'current_user': current_user,
            }
            return render(request, 'hospitalPage.html', context)

        if usertype == "AMBULANCE":
            nuser = ambulance.objects.filter(email=email, password=password)
            if not nuser:
                messages.error(
                    request, 'username or password are invalid (:\n Please try again')
                return redirect('login')
            current_user = ambulance.objects.get(email=email)
            context = {
                'current_user': current_user,
            }
            return render(request, 'ambulancePage.html', context)
    return render(request, 'login.html')


def patient1(request):

    if request.method == "POST":
            try:
                fname = request.POST['fname']
                midname = request.POST['midname']
                lname = request.POST['lname']
                dateOfRequest = request.POST['dateOfRequest']
                timeOfRequest = request.POST['timeOfRequest']
                am_pm = request.POST['am_pm']
                email = request.POST['email']
                phNo = request.POST['phNo']
                pickupStreet = request.POST['pickupStreet']
                pickupCity = request.POST['pickupCity']
                pickupState = request.POST['pickupState']
                pickupZip = request.POST['pickupZip']
                desstreet = request.POST['desstreet']
                descity = request.POST['descity']
                desstate = request.POST['desstate']
                desZip = request.POST['desZip']
                dob = request.POST['dob']
                gender = request.POST['gender']
                relation = request.POST['relation']
                medical_con = request.POST['medical_con']
                resonForAmb = request.POST['resonForAmb']

                User_gmail = user.objects.get(
                    email=request.session.get('email'))

                ambulance1 = request.POST['ambulance']
                #o = ambulance.objects.get(name=ambulance1)
                # o = av_ambulance.objects.get(name=ambulance1)
                # av_hospital1 = av_ambulance.objects.get(email=o.email)
                
                # AvAmb_gmail = av_hospital1
                # Amb_gmail = av_hospital1

                p = patient(fname=fname, midname=midname, lname=lname, dateOfRequest=dateOfRequest, timeOfRequest=timeOfRequest, am_pm=am_pm, email=email, phNo=phNo, pickupStreet=pickupStreet, pickupCity=pickupCity,pickupState=pickupState, pickupZip=pickupZip, desstreet=desstreet, descity=descity, desstate=desstate, desZip=desZip, dob=dob, gender=gender, relation=relation, medical_con=medical_con, resonForAmb=resonForAmb, User_gmail=User_gmail)
                p.save()
                messages.success(
                    request, 'Your ambulance'+str(ambulance1)+' has been successfuly booked')
            except (KeyError, hospital.DoesNotExist, av_hospital.DoesNotExist, user.DoesNotExist):
                messages.error(
                request, 'Invalid form submission. Please check the entered values.')
    
    return render(request, 'userPage.html')


def hos_patient1(request):
    if request.method == "POST":
        try:
            fname = request.POST['fname']
            midname = request.POST['midname']
            lname = request.POST['lname']
            dateOfRequest = request.POST['dateOfRequest']
            timeOfRequest = request.POST['timeOfRequest']
            am_pm = request.POST['am_pm']
            email = request.POST['email']
            phNo = request.POST['phNo']
            Street = request.POST['Street']
            City = request.POST['City']
            State = request.POST['State']
            Zip = request.POST['Zip']
            dob = request.POST['dob']
            gender = request.POST['gender']
            relation = request.POST['relation']
            medical_con = request.POST['medical_con']
            resonForHos = request.POST['resonForHos']
            hospital1 = request.POST['hospital']
            o = hospital.objects.get(name=hospital1)
            av_hospital1 = av_hospital.objects.get(email=o.email)
            emailz = user.objects.get(email=request.session.get('email'))
            p = hos_patient(User_gmail=emailz, fname=fname, midname=midname, lname=lname, dateOfRequest=dateOfRequest, timeOfRequest=timeOfRequest, am_pm=am_pm, email=email, phNo=phNo, Street=Street, City=City,
                            State=State, Zip=Zip, dob=dob, gender=gender, relation=relation, medical_con=medical_con, resonForHos=resonForHos, hospital=hospital1, AvHospital_gmail=av_hospital1)
            p.save()
            messages.success(
                request, 'Your hospital'+str(hospital1)+ 'has been successfuly booked at '+str(dateOfRequest)+str(timeOfRequest))
        except (KeyError, hospital.DoesNotExist, av_hospital.DoesNotExist, user.DoesNotExist):
            messages.error(
                request, 'Invalid form submission. Please check the entered values.')

    return render(request, 'hos_bookingform.html')


def view_amb_booking(request):
    c_gmail = request.session['email']
    view_p = patient.objects.filter(User_gmail=c_gmail).values()
    context = {
        'view_p': view_p,
    }
    return render(request, 'view_amb_booking.html', context)


def view_hos_booking(request):
    c_gmail = request.session['email']
    view_p = hos_patient.objects.filter(User_gmail=c_gmail).values()

    context = {
        'view_p': view_p,
    }

    return render(request, 'view_hos_booking.html', context)


def avAmbulance(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phNo = request.POST['phNo']
        Street = request.POST['Street']
        City = request.POST['City']
        State = request.POST['State']
        Zip = request.POST['Zip']
        NoOfAmb = request.POST.get('NoOfAmb')
        a = av_ambulance(name=name, email=email, phNo=phNo, Street=Street, City=City,
                         State=State, Zip=Zip, NoOfAmb=NoOfAmb)
        a.save()

        return render(request, 'am_booking.html')


def hos_view(request):
    obj = hos_patient.objects.filter(
        AvHospital_gmail=request.session['email']).values()
    return render(request, 'hos_view.html', {'obj': obj})


def amb_view(request):
    obj = patient.objects.filter(AvAmb_gmail=request.session['email']).values()
    return render(request, 'amb_view.html', {'obj': obj})


def nearby_hos(request):

    # Retrieve the city of the ambulance from the database
    ambulance = av_ambulance.objects.get(
        email=request.session['email'])
    city = ambulance.City

    # Retrieve all hospitals located in the same city as the ambulance
    hospitals = av_hospital.objects.filter(City=city)
    # Construct a list of hospital names and their addresses
    hospital_list = []
    for hospital in hospitals:
        hospital_name = hospital.name
        hospital_address = hospital.Street + ", " + hospital.City + \
            ", " + hospital.State + " " + hospital.Zip
        hospital_list.append((hospital_name, hospital_address))

    # Render the list of hospitals in a template
        obj = {'hospital_list': hospital_list}
    return render(request, 'nearby_hos.html', obj)


def nearby_hos_usr(request):

    # Retrieve the city of the user from the database
    users = user.objects.get(
        email=request.session['email'])

    if request.method == 'GET':
        city = request.GET.get('city')
        if city:
            # Retrieve all hospitals located in the same city as the search city
            hospitals = av_hospital.objects.filter(City__icontains=city)
    # Construct a list of hospital names and their addresses
            hospital_list = []
            for hospital in hospitals:
                hospital_name = hospital.name
                hospital_address = hospital.Street + ", " + hospital.City + \
                    ", " + hospital.State + " " + hospital.Zip
                hospital_list.append((hospital_name, hospital_address))

    # Render the list of hospitals in a template
            obj = {'hospital_list': hospital_list}
        return render(request, 'nearbyhos_usr.html', obj)
    else:
        return render(request, 'search_hospital.html', obj)


def emergency_create(request):
    if request.method == 'POST':
        # Create a new Emergency object with the submitted data
        emergency = Emergency()
        emergency.current_address = request.POST.get('current_address')
        emergency.destination_address = request.POST.get('destination_address')
        emergency.city=request.POST.get('city')
        city=emergency.city
        print(city)

        emergency.save()
        print(city)
        # Assign an available ambulance from the same city as the emergency

        available_ambulances = list(av_ambulance.objects.filter(City__icontains=city))
        print(available_ambulances)
        if available_ambulances:
            ass_amb=available_ambulances[0]
            print(ass_amb)
            messages.success(
                request, 'Emergency booking successful. Ambulance assigned.your ambulance is:'+str(ass_amb))
            #emergency.save()

        # Redirect to the emergency detail page
        return redirect('emg_booking')
    else:
        form = EmergencyForm()
        return render(request, 'emg_booking', {'form': form})
