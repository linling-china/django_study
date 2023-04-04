from django.shortcuts import render
from .forms import LoginForm, RegistrationForm, UserAddedForm, UserForm, UserInfoForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserAdded, UserInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid() :
            cd = login_form.cleaned_data
            user = authenticate(**cd) #直接将字典转换为关键字参数.
            if user :
                login(request, user)
                return HttpResponse('Login success!!')
            else :
                return HttpResponse('LOGIN ERROR : password or username error...')
        else :
            return HttpResponse('ERROR : INVALID LOGIN DATA .')
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/user_login.html', {'formm':login_form})

def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        user_form_added = UserAddedForm(request.POST)
        if user_form.is_valid() and user_form_added.is_valid():
            new_user = user_form.save(commit=False)
            #请不要试图直接操作用户的密码，数据库保存的是hash转换的结果，所以创建用户需要辅助函数的原因。
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            new_user_added = user_form_added.save(commit=False)
            new_user_added.user = new_user #写入一对一关联的user对象
            new_user_added.save()
            return HttpResponse('SUCCESS!')
        else:
            #items转list然后合并.可以直接将报错输出到前端.
            return HttpResponse(list(user_form_added.errors.items())+list(user_form.errors.items()))
    else:
        user_form = RegistrationForm()
        user_form_added = UserAddedForm()
        return render(request, 'account/register.html', {"form" : user_form, "form_added" : user_form_added})

@login_required()
def self_info(request):
#   return HttpResponse([each+'<br>' for each in dir(request.user)]) #打印出user对象的所有属性
#   return HttpResponse([each+'<br>' for each in dir(request.user.userinfo)])
    u = request.user
    useradded = UserAdded.objects.get(user=request.user) if hasattr(u, 'useradded') else UserAdded.objects.create(user=u)
    userinfo  = UserInfo.objects.get(user=u) if hasattr(u, 'userinfo') else UserInfo.objects.create(user=u)
    return render(request, 'account/selfinfo.html', {'user':request.user, 'useradded':useradded, 'userinfo':userinfo})

def selfinfo_edit(request):
    userinfo, b = UserInfo.objects.get_or_create(user=request.user)
    useradded, b = UserAdded.objects.get_or_create(user=request.user)
    if request.method == 'POST':
#        print(request.POST)
        user_form = UserForm(request.POST, instance=request.user)#绑定数据指定实例instance
        useradded_form = UserAddedForm(request.POST, instance=useradded)
        userinfo_form = UserInfoForm(request.POST,instance=userinfo)
        if user_form.is_valid() and useradded_form.is_valid() and userinfo_form.is_valid() :
            user_form.save()
            useradded_form.save()
            userinfo_form.save()
            return HttpResponseRedirect('/account/selfinfo/')
        else :
            return HttpResponse(list(user_form.errors.items()) + list(useradded_form.errors.items()) + list(userinfo_form.errors.items()))
        # user_form_data = user_form.cleaned_data
           # useradded_form_data = useradded_form.cleaned_data
           # userinfo_form_data = userinfo_form.cleaned_data
    if request.method == 'GET':
        user_form = UserForm(instance=request.user) #带入初始值有两个方法，1.instance 2.initial
        useradded_form = UserAddedForm(instance=useradded)
        userinfo_form = UserInfoForm(instance=userinfo)
        return render(request, 'account/selfinfo_edit.html',
                      {"user_form":user_form, "useradded_form":useradded_form, "userinfo_form":userinfo_form})

def selfimage_edit(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else :
        return render(request, 'account/imagecrop.html')