from django.shortcuts import render
from django.http import HttpResponse
from . models import Login
from . models import Sgup
from . models import Profilepic

# Create your views here.

# def fn_index1( request):
#     return HttpResponse('Working.....')

# def fn_test( request):
#     # if request.method=='POST':
#     #     print(request.POST)
#     #     name=request.POST['name']
#     #     print(name)
#     #     return HttpResponse(name)
#     return render(request,'test.html',{'msg':'my test page loaded'})


# def fn_getData(request):
#     print(request.POST)
#     name=request.POST['name']
#     print(name)
#     return HttpResponse(name)


def fn_login(request):
    return render(request,'index.html')

####### Login ###########################

def fn_userData( request):
    uname = request.POST['username']
    password = request.POST['password']
    try:
        login_obj = Login.objects.get(username=uname)
        # print(login_obj.password)
        if password == login_obj.password:
            request.session['user_id'] = login_obj.id
            # u_id = request.session['user_id']
            reg = Sgup.objects.get(login=login_obj.id)
            propic = Profilepic.objects.get(login=login_obj.id)
            reg.userimage=propic.image
            return render(request,'timeline.html',{'user':reg})
            # return HttpResponse('logined')
        return render(request, 'login2.html',{'username':uname})
        # return HttpResponse('password error')
    except Exception as e:
        print(str(e))
        # return HttpResponse('username error')
        return render(request, 'login.html')


######## Registraion ######################
 
 
def fn_signup(request):
    if request.method == 'POST':
        email = request.POST['username']
        user_exist = Login.objects.filter(username=email).exists()     
        if not user_exist:
            fname = request.POST['fname']
            sname = request.POST['surname'] 
            signpass = request.POST['pswd']
            dob = request.POST['year']+ "-" +request.POST['month']+ "-" +request.POST['day']
            gender = request.POST['gender']
            try:
                sign_obj = Login(username=email, password=signpass)
                sign_obj.save()
                if sign_obj.id > 0:
                    insert_data=Sgup(firstname=fname, surname=sname,dob=dob, gender=gender, login=sign_obj)
                    insert_data.save()
                    if insert_data.id > 0:
                        return render(request,'login2.html',{'username':email} )
                        # return HttpResponse('logined')
            except Exception as e:
                print(str(e))
                # return render(request,'index.html')
                return HttpResponse('no reg')
        return HttpResponse("username already exist")
    # return request(request,'index.html')
    return HttpResponse('invaid')


######### Change Password ##################

# def fn_change_pass(request):
#     if request.method == "POST":
#         user_id = request.session['user_id']
#         # print('session id:',user_id)
#         exist_password = request.POST['current']
#         # print('current password:'+exist_password)
#         new_password = request.POST['change']
#         # print('new password:' +new_password)
#         login = Login.objects.get(id=user_id)
#         # print(login.password)
#         if exist_password == login.password:
#             login.password = new_password
#             login.save()
#             return render(request,'changepswd.html',{'msg':'Password Changed Successfully'})
#             # return HttpResponse('success')
#         else:
#             # return HttpResponse('invalid')
#             return render(request,'changepswd.html',{'msg':'Your current password wrong'})
#     return render(request,'changepswd.html') 

###############################################################

def fn_update(request):
    return render(request,'test.html')

def fn_updatepass(request):
    user_id = request.session['user_id']
    print(user_id)
    cpass=request.POST.get('cur_password')
    npass=request.POST.get('new_password')
    print(cpass)
    print(npass)

    login = Login.objects.get(id=user_id)

    if cpass == login.password:
        login.password = npass
        login.save()
        # return render(request,'changepswd.html',{'msg':'Password Changed Successfully'})
        return HttpResponse('success')

    # return HttpResponse('invalid')
        # return render(request,'changepswd.html',{'msg':'Your current password wrong'})

    # return HttpResponse('success')

#######################################################

########## Edit Profile#####################


# def fn_editprofile(request):
#     u_id = request.session['user_id']
#     reg = Sgup.objects.get(login=u_id)

#     try:
#         if request.method=='POST':
#             fname = request.POST['firstname']
#             lname = request.POST['lastname']
#             reg.firstname = fname
#             reg.surname = lname
#             reg.save()
#         return render(request,'editprofile.html',{'user':reg})
#     except Exception as e:
#         print(str(e))
#         return HttpResponse('not changed')
#     return render(request,'editprofile.html',{'user':reg})

def fn_chpass(request):
    return render(request,'changepswd.html')




def fn_editprofile(request):
    my_id = request.session['user_id']
    reg = Sgup.objects.get(login=my_id)
    log = Login.objects.get(id=my_id)
    try:
        if request.method == 'POST':
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            reg.firstname = fname
            reg.surname = lname
            reg.save()
            if request.FILES:
                myfile = request.FILES['image_upload']
                propic = Profilepic.objects.get(login=my_id)
                propic.image = myfile
                propic.save()
        image_obj = Profilepic.objects.get(login=my_id)
        reg.userimage = image_obj.image
        return render(request,'editprofile.html',{'user':reg})
    except Exception as e:
        print('image does not exist')
        if request.method == 'POST':
            obj_propic = Profilepic(image=myfile,login=log)
            obj_propic.save()
            reg.userimage = obj_propic.image
        return render(request,'editprofile.html',{'user':reg})

