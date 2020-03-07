from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.
def index(request):
    num=10;
    name='luwei';
    namelist=['lu','wei','yao','ting']
    d1={'name':'haha','age':18,'email':'66@163.com','DL':namelist}
    maxsize=12347612
    time_now=datetime.datetime.now()
    d2=[[11,22],[33,44],[55,66],[77,88]]
    d3=['aa','bb','cc','dd','ee']
    words='i love you haha lala'
    tag= '<a href="http://www.baidu.com">百度</a>'
    class DEMO:
        def __init__(self):
            self.kind='cat';
        def eat(self):
            return 'yuyuyu'
    demo=DEMO()
    return render(request,'index.html',locals())
    # return render(request,'index.html',{'num':num,'name':name,'namelist':namelist,'d1':d1,'demo':demo})

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        # print(request.POST.get.user,request.POST.get.psd)
        print(request.body)
        print(request.POST.get('user'))
        # return HttpResponse('登录成功!!!!')
        return render(request,'login2.html')