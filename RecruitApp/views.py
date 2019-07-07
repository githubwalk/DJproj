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
    message['jobList'] = jobList

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
            request.session['state'] = True
            request.session['email'] = perEmail
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

def perSchedule(request): #璇 07/07
    '''
    用户单击 '企业反馈' 或 '公司查看' 进入简历状态页面(投递成功 or 被查看)
    input:status
    output:schedule.html or secheduleViewed.html
    '''
    val = request.session.get('state', False)
    if val:
        perEmail = request.get_signed_cookie('account', '', salt='asds')
        obj = models.PerInfo.objects.get(perEmail=perEmail)
        applyPer = obj.perUser
        dlist = models.ApplyList.objects.filter(applyPer=applyPer)
        return render(request, 'schedule.html', {'dlist':dlist})
    else:
        return render(request, 'login.html')


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
def ApplyOne(inputUserId,inputJobId):
    '''
    多简历投递清单写入数据库辅助函数，写入一条简历投递清单
    input:inputUserId,inputJobId
    output:bool
    '''
    if inputUserId == None or inputJobId == None:
         return False
    if models.ApplyList.objects.filter(applyPer=inputUserId, applyJob=inputJobId):#重复了就不添加
        return True
    else:
        aOne= models.ApplyList(applyPer=inputUserId,applyJob=inputUserId)
        if aOne.save():
            return True

def applyCheckedJobs(request):#ajax post请求
    '''
    用户单击"一键投递"多简历投递清单写入数据库并提示成功/失败信息
    input:
    output:bool or index.html
    '''
    if request.POST:
        inputUserId=request.POST.get('inputUserId',None)#获取用户id
        inputJobIDList=request.POST.getlist('inputJobIDList',None)#获取申请公司id
        for inputJobId in inputJobIDList:
            ApplyOne(inputUserId,inputJobId)#存入数据库
        return HttpResponse(True)#返回ajax为true
    else:#返回默认页
        return render(request,'index.html')

# end

# 骅 07/07
def recruit(request,currentCity,jobId):
    '''
    用户单击首页热门职位按钮进入招聘职位详情页
    input:
    output:recriut.html
    '''
    if request.POST:
        inputUserId=request.POST.get('inputUserId',None)#获取用户id
        inputJobId=jobId#获取申请公司id
        if ApplyOne(inputUserId,inputJobId):#复用写入一条简历投递清单
            return render(request,'recruit.html',{'msg':'投递成功！'})
        else:
            return render(request,'recruit.html',{'msg':'投递失败！'})
    else:
        # 获取当前职位对象信息
        job=models.Job.objects.filter(id=jobId)
        # 存入字典
        recruit = dict()
        recruit['compUser']=job[0].compUser
        recruit['jobName']=job[0].jobName
        recruit['jobProfession']=job[0].jobProfession
        recruit['jobSalary']=job[0].jobSalary
        recruit['jobEdu']=job[0].jobEdu
        recruit['jobExp']=job[0].jobExp
        recruit['jobNum']=job[0].jobNum
        recruit['jobSkill']=job[0].jobSkill
        recruit['jobPublishedTime']=job[0].jobPublishedTime
        recruit['jobIntro']=job[0].jobIntro
        recruit['jobClickNum']=job[0].jobClickNum
        recruit['currentCity']=currentCity
        return render(request,'recruit.html',recruit)#返回信息并显示
# end

# 魏 07/07
def search(request):
    return render(request,'search.html')
# end




# 刘 7/7
from .models import Question, Answer, Review, CollectList, LikeList, PerUser, PerInfo
from django.urls import reverse
def postQuestion(quesAuthor, quesTitle, quesContent):
    '''
    发表一个问题
    :param quesAuthor:
    :param quesTitle:
    :param quesContent:
    :return: 问题id（int）
    '''
    question = Question(quesAuthor=quesAuthor, quesTitle=quesTitle,
                    quesContent=quesContent)
    question.save()
    return question.id

def collectQuestion(collPerUser, collQuestion):
    '''
    收藏一个问题
    :param collPerUser:
    :param collQuestion:
    :return: True为收藏False取消收藏，当前收藏数
    '''
    matchSet = CollectList.objects.filter(collPerUser=collPerUser,
                                          collQuestion=collQuestion)
    if len(matchSet) == 0:
        CollectList.objects.create(collPerUser=collPerUser,
                                          collQuestion=collQuestion)
        collNum = len(CollectList.objects.filter(collQuestion=collQuestion))
        return True, collNum
    else:
        matchSet[0].delete()
        collNum = len(CollectList.objects.filter(collQuestion=collQuestion))
        return False, collNum

def answerQuestion(ansAuthor, ansQuestion, ansContent):
    Answer.objects.create(ansAuthor=ansAuthor, ansQuestion=ansQuestion,
                          ansContent=ansContent)

def likeAnswer(likePerUser, likeAnswer):
    matchSet = LikeList.objects.filter(likeAnswer=likeAnswer,
                                       likePerUser=likePerUser)

    if len(matchSet) == 0:
        LikeList.objects.create(likeAnswer=likeAnswer,
                                       likePerUser=likePerUser)
        likeNum = len(LikeList.objects.filter(likeAnswer=likeAnswer))
        return True, likeNum
    else:
        matchSet[0].delete()
        likeNum = len(LikeList.objects.filter(likeAnswer=likeAnswer))
        return False, likeNum

def postReview(revAuthor, revAnswer, revContent):
    Review.object.create(revAuthor=revAuthor, revAnswer=revAnswer,
                         revContent=revContent)

def getPerUserFromSession(request):
    userEmail = request.session.get('email')
    perUserObject = PerInfo.objects.get(perEmail=userEmail).perUser
    return perUserObject


class QuestionDisplayer():
    def __init__(self, question, request=None):
        '''
        存储论坛首页问题展示的信息
        :param question: 问题对象
        '''
        self.id = question.id
        self.title = question.quesTitle
        self.author = question.quesAuthor
        self.readCount = question.quesReadCount
        self.answerCount = len(Answer.objects.filter(ansQuestion=question))
        self.createTime = question.quesCreateTime
        self.answers = Answer.objects.filter(ansQuestion=question).order_by('-ansCreateTime')
        self.bestAnswer = AnswerDisplayer(self.answers[0], request) if len(self.answers)!=0 else None # 是一个AnswerDisplayer
        try:
            print(self.bestAnswer.ansAuthor.perinfo.perHeadPath,"========================================================")
        except Exception:
            pass

class AnswerDisplayer():
    def __init__(self, Answer, request):
        self.id = Answer.id
        self.content = Answer.ansContent
        self.author = Answer.ansAuthor
        self.createTime = Answer.ansCreateTime
        self.likeCount = len(LikeList.objects.filter(likeAnswer=Answer))
        self.isLiked = len(LikeList.objects.filter(likePerUser=getPerUserFromSession(request))) != 0



def forumIndex(request):
    # request.session['email'] = '123@qq.com'  # 本人测试用，可以删
    print(request.session['email'])
    para = {}
    para['websiteIconPath'] = "https://www.baidu.com/img/baidu_jgylogo3.gif"  # 测试用，网页logo
    para['msgNum'] = 10   # 测试用，用户的未查看消息提示
    displayQuestions = Question.objects.order_by('-quesCreateTime')
    para['problems'] = [QuestionDisplayer(question, request) for question in displayQuestions]
    para['userHeadIcon'] = '/static/' + getPerUserFromSession(request).perinfo.perHeadPath
    return render(request, 'forumIndex.html', para)

def postQuestionView(request):
    '''相应发布的问题'''
    if request.method == "POST":
        quesTitle = request.POST.get('title', '')
        quesContent = request.POST.get('content', '')
        quesAuthor = getPerUserFromSession(request)
        questionId = postQuestion(quesAuthor, quesTitle, quesContent)
        return redirect(reverse('questionPage', kwargs={'questionId': questionId}))
    else:
        return redirect(reverse('forumIndex'))

def likeView(request, answerId):
    '''响应点赞操作'''
    likePerUserObject = getPerUserFromSession(request)
    likeAnswerObject = Answer.objects.filter(id=answerId)[0]
    likeOrCancel, likeNum = likeAnswer(likePerUserObject, likeAnswerObject)
    return HttpResponse(str(likeOrCancel) + ';' + str(likeNum))



def questionPage(request, questionId):
    # 弄一下阅读数
    questionObject = Question.objects.get(id=questionId)
    questionObject.quesReadCount += 1
    questionObject.save()
    return HttpResponse('questionPage: %d' % questionId)

def userPage(request):
    return HttpResponse('userpage')

# end