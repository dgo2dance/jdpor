from django.http import HttpResponse
from .models import MyappJd
from .forms import RegisterForm,UserForm
from .models import HhhhUser
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
'''改变数据库结构函数，用于计算三个品类中降幅比最高的前三款。
如果数据库中的数据有变化，那么就要访问http://127.0.0.1:8000/myapp/change/,调用这个函数，从而计算前三款商品。如果数据库数据没有变化，则不用访问'''
def change(request):
    # 将数据从数据库中取出
    goods = MyappJd.objects.filter()
    # 循环拿取每条数据中的十天价格
    for i in goods:
        list = []
        '''将这十天的价格一依次，因为是存的字符串，所以转成数字，方便计算'''
        a = float(i.number_3_05)
        b = float(i.number_3_06)
        c = float(i.number_3_07)
        d = float(i.number_3_08)
        e = float(i.number_3_09)
        f = float(i.number_3_10)
        g = float(i.number_3_11)
        n = float(i.number_3_12)
        h = float(i.number_3_13)
        j = float(i.number_3_14)
        k = float(i.number_3_15)
        '''将10天价格存入列表'''
        list = [a,b,c,d,e,f,g,n,h,j,k]
        t = max(list)   #获取十天中价格最高的值
        loss =(1- (k / t))  #用最高的价格除去最后一天
        loss = loss * 100   #得出百分比
        loss = '%.2f' %loss
        if len(loss) == 4:
            loss = "0" + str(loss)
        id = i.id   #然后获取商品的id
        hero = MyappJd.objects.get(id=id)
        hero.max_today = loss
        hero.save() #存入数据库

        print(list,t,loss,id,hero.id,len(loss))

    return HttpResponse("修改完成")

# 这是主页函数
def find(request):

    return render(request,"bbb.html")

# 手机商品页
def phone(request):
    goods = MyappJd.objects.filter(types="手机").order_by('-max_today')[:3]   #降序以后，取前三条数据
    data = {
        'goods': goods,
    }
    return render(request, "phone.html", context=data)

# 电脑商品页
def computer(request):
    computers = MyappJd.objects.filter(types="电脑").order_by('-max_today')[:3]   #降序以后，取前三条数据
    data = {
        'computers':computers,
    }
    return render(request, "computer.html", context=data)

# 耳机商品页
def ear(request):
    ears = MyappJd.objects.filter(types="耳机").order_by('-max_today')[:3]    #降序以后，取前三条数据
    data = {
        'ears':ears
    }
    return render(request, "ear.html", context=data)


# 商品详情页
def detail(request,id):
    products = MyappJd.objects.filter(id=id)
    data = {
        'products':products,
    }
    #return HttpResponse("1")
    return render(request,'detail.html',context=data)

#登录界面，session判断是否已经登录，表单验证
def login(request):

    if request.session.get('is_login', None):
        return redirect(reverse('myapp:find'))

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user =HhhhUser.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name

                    return redirect(reverse('myapp:find'))
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
                return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())

#注册界面，表单验证，存入数据库，密码无加密
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("myapp:index")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = HhhhUser.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'account.html', locals())
                same_email_user = HhhhUser.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'account.html', locals())
                # 当一切都OK的情况下，创建新用户
                new_user = HhhhUser()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect(reverse('myapp:login'))  # 自动跳转到登录页面

    register_form = RegisterForm()
    return render(request, 'account.html', locals())

#退出界面
def logout(request):
    if not request.session.get("is_login" ,None):
        return redirect(reverse('myapp:find'))
    request.session.flush()
    return redirect(reverse("myapp:find"))
