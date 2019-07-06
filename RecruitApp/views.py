from django.shortcuts import render, redirect


from RecruitApp import models
import uuid
import hashlib
from django.core.mail import send_mail, send_mass_mail
from DJproj import settings
from django.http import HttpResponse


# 07/06 11:33 add by 黄涣升

#主页
def index(request, currentCity):
    '''
    Get_input: currentCity;
    return_msg: message(一个字典, 用于传递信息回前端)
    return: 
    '''
    # inputUserId = PerUser.objects.get('id')
    jobList = models.Job.objects.all()
    # 根据用户简历输入的城市、薪资、……把列表筛选出新的列表
    # 再根据点击数降序排列
    # TODO
    message = dict()
    message['currentCity'] = currentCity

    if request.POST:
        return HttpResponse('这里是搜索结果')
    else:
        return render(request, 'index.html', message)



def gotoClickedProfession(request,name):
    '''
    根据点击的职位跳转到职位搜索界面
    :param name
    :return: 根据点击的职位，返回拼接后的页面url
    '''
    result = '{0}'.format(name) + '.html'
    return render(request,result)

# end

# 07/06 10:08 add by 黄涣升
# 关于
# 关于-本司招聘
def aboutusAbout(request):
    return redirect('https://special.zhaopin.com/sh/2009/aboutus/about.html')
    
# 关于-人才招聘
def jobsZhaoPin(request):
    return redirect('https://jobs.zhaopin.com/')

# 关于-联系方式
def aboutusContact(request):
    return redirect('https://jobs.zhaopin.com/')


# 关于-网站地图
def siteMap(request):
    return redirect('https://jobs.zhaopin.com/')

# 帮助
# 帮助-加入我们
def joinUs(request):
    return redirect('https://jobs.zhaopin.com/')

# 帮助-客户服务
def customerService(request):
    return redirect('https://jobs.zhaopin.com/')

# 帮助-法律声明
def law(request):
    return redirect('https://jobs.zhaopin.com/')

# 帮助-隐私政策
def secrecy(request):
    return redirect('https://jobs.zhaopin.com/')

# 帮助-发票制度
def invoiceSystem(request):
    return redirect('https://jobs.zhaopin.com/')
# end



# 唐 07/06
def getCode():
    '''
    生成随机验证码
    input:
    output: 验证码
    '''
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

def sendCode(request, perEmail):
    '''
    发送验证码
    input: email
    output:
    '''
    title = "大佬鼠招聘验证码"
    code = getCode()
    request.session['code'] = code
    msg = "请将 " + code + " 填入注册页面以继续注册。"
    emailFrom = settings.DEFAULT_FROM_EMAIL
    # 发送邮件
    try:
        send_mail(title, msg, emailFrom, perEmail, fail_silently=False)
    except:
        return HttpResponse(False)
    return HttpResponse(True)


def register(request):
    if request.POST:
        perEmail = request.POST.get('perEmail', None)
        perCode = request.POST.get('perCode', None)
        code = request.session.get('code', '')
        if perCode == code:
            return render(request, 'registerStep1.html')
        else:
            return render(request, 'register.html', {'msg': '验证码错误'})
    else:
        return render(request, 'register.html')



def login(request):
    '''
    登录
    input:
        perEmail
        perPwd
    output:
        成功：返回首页
        失败：提示信息
    '''
    if request.POST:
        # 获取输入的email
        perEmail = request.POST.get('perEmail', None)
        print(perEmail)
        # 获取输入的密码
        perPwd = request.POST.get('perPwd', None)
        # 取出email对应对象
        obj = models.PerInfo.objects.filter(perEmail=perEmail)  # 没问题的
        print(obj)
        print(type(obj))
        if len(obj) == 0:
            # 账号不存在
            return render(request, 'login.html', {'msg': '账号不存在'})
        elif obj[0].perPwd != perPwd:
            # 密码错误
            return render(request, 'login.html', {'msg': '密码错误'})
        else:
            # 登录成功
            perCity = obj[0].perCity
            request.session[obj[0].perUser.id] = {'state': True}
            re = 'RecruitApp/' + str(perCity) + '/'
            response = render(request, 'RecruitApp.html')
            response.set_signed_cookie('account', perEmail, salt='asds')
            return response
    else:
        perEmail = request.get_signed_cookie('account', '', salt='asds')
        return render(request, 'login.html',{'perEmail': perEmail})
# end


# 璇 07/06
def perResume(request):
    '''
    用户单击 头像 or 我的简历 进入个人简历页面
    input:
    output:resume.html
    '''
    return render(request, 'resume.html')

def perSchedule(request):
    '''
    用户单击 '企业反馈' 或 '公司查看' 进入简历状态页面(投递成功 or 被查看)
    input:status
    output:schedule.html or secheduleViewed.html
    '''
    # get用户要查看的状态
    val = request.GET.get('status', 0)
    # 用户单击'企业反馈' status = 0 进入投递成功页面
    if val == 0:
        return render(request, 'schedule.html')
    # 用户单击'公司查看' status = viewed 进入被查看页面
    else:
        return render(request, 'secheduleViewed.html')

def resumeModels(request):
    '''
    用户单击'简历模板' 进入简历模板页面
    input:
    output:resumeModels.html
    '''
    return render(request, 'resumeModels.html')

def workHotspots(request, num):
    '''
    用户单击'职场热点'中的问题连接
    input:num 问题序号
    output:question+num.html
    '''
    # 拼接要进入的页面
    result = 'question' + '{0}'.format(num) + '.html'
    # 进入对应问题页面
    return render(request,result)
# end



# 骅 07/06
def ApplyOne(inputUserId,inputJobID):
    if inputUserId == None or inputJobID == None:
         return False
    if models.ApplyList.objects.filter(applyPer=inputUserId, applyJob=inputJobID):#重复了就不添加
        return True
    else:
        aOne= models.ApplyList(applyPer=inputUserId,applyJob=inputUserId)
        if aOne.save():
            return True

def applyCheckedJobs(request):#ajax post请求
    if request.POST:
        inputUserId=request.POST.get('inputUserId',None)#
        inputJobIDList=request.POST.getlist('inputJobIDList',None)#获取申请公司
        for inputJobId in inputJobIDList:
            ApplyOne(inputUserId,inputJobId)#存入数据库
        return HttpResponse(True)#返回ajax为true
    else:#返回默认页
        return render(request,'index.html')

# end