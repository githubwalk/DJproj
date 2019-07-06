from django.db import models

# parameter
max_length = 50

# Create your models here.
class PerUser(models.Model):
    '''
    个人用户类
    '''
    perOthers = models.TextField()

    def __str__(self):
        return self.perinfo.perName

class CompUser(models.Model):
    '''
    企业用户
    '''

    def __str__(self):
        return self.compinfo.compFullName

class PerInfo(models.Model):
    '''
    个人信息类
    '''
    perUser = models.OneToOneField(PerUser, on_delete=models.CASCADE)
    perEmail = models.EmailField()                      # 邮箱
    perPwd = models.CharField(max_length=max_length)    # 密码
    perName = models.CharField(max_length=max_length)   # 姓名
    perSex = models.BooleanField()                      # 性别 True: 男; False: 女.
    perBirth = models.DateField()                       # 出生日期
    perHeadPath = models.CharField(max_length=max_length) # 头像
    perCity = models.CharField(max_length=max_length)   # 居住城市
    perWorkStartTime = models.DateField()               # 参加工作时间


class PerEdu(models.Model):
    '''
    教育经历类
    '''
    perUser = models.OneToOneField(PerUser, on_delete=models.CASCADE)
    perSchool = models.CharField(max_length=max_length) # 学校名称
    perStatus = models.CharField(max_length=max_length) # 学历
    perMajor = models.CharField(max_length=max_length)  # 专业
    perStudyStartTime = models.DateField()              # 就读开始时间
    perStudyEndTime = models.DateField()                # 就读结束时间


class PerWorkExp(models.Model):
    '''
    工作经验类
    '''
    perUser = models.ForeignKey(PerUser, on_delete=models.CASCADE)
    perComp = models.ForeignKey(CompUser, on_delete=models.CASCADE)
    perProfession = models.CharField(max_length=max_length) # 所属行业
    perJob = models.CharField(max_length=max_length)        # 职位名称
    perStart = models.DateField()                           # 在职起始时间
    perEnd = models.DateField()                             # 终止时间
    perSalary = models.IntegerField()                       # 月薪
    perDescription = models.TextField()                     # 工作描述


class PerExpected(models.Model):
    '''
    求职意向类
    '''
    perUser = models.OneToOneField(PerUser, on_delete=models.CASCADE)
    perExpectedJob = models.CharField(max_length=max_length)            # 期望行业
    perExpectedProfession = models.CharField(max_length = max_length)   # 期望职类
    perExpectedSalary = models.IntegerField()                           # 期望月薪


class CompInfo(models.Model):
    '''
    公司信息
    主键为自动生成的id
    '''
    compUser = models.OneToOneField(CompUser, on_delete=models.CASCADE)  # 企业用户(外键)
    compFullName = models.CharField(max_length=max_length)  # 单位全称
    compLogoPath = models.CharField(max_length=max_length)  # 公司logo路径
    compVideoPath = models.CharField(max_length=max_length)  # 公司介绍视频路径
    compProfession = models.CharField(max_length=max_length)  # 公司
    compCity = models.CharField(max_length=max_length)  # 城市
    compLoc = models.CharField(max_length=max_length)  # 地址
    compIntro = models.TextField()  # 简介
    compPwd = models.CharField(max_length=max_length)  # 密码
    compEmail = models.EmailField()  # 邮箱

    def __str__(self):
        return self.compFullName


class Job(models.Model):
    '''
    职位
    主键是自动生成的id
    '''
    compUser = models.ForeignKey(CompUser, on_delete=models.CASCADE)  # 企业用户(外键)
    jobName = models.CharField(max_length=max_length)  # 名称
    jobProfession = models.CharField(max_length=max_length)  # 行业类型
    jobSalary = models.IntegerField()  # 月薪
    jobEdu = models.CharField(max_length=max_length)  # 学历要求
    jobExp = models.CharField(max_length=max_length)  # 经验要求
    jobNum = models.IntegerField()  # 招聘人数
    jobSkill = models.CharField(max_length=max_length)  # 技能要求
    jobPublishedTime = models.DateField(auto_now_add=True)  # 发表时间,自动保存创建时间，后面不可再次更改
    jobIntro = models.TextField()  # 职位描述
    jobClickNum = models.IntegerField()  # 点击数

    def __str__(self):
        return self.jobName




class ApplyList(models.Model):
    '''
    简历投递清单(申请清单）
    '''
    applyPer = models.ForeignKey(PerUser, on_delete=models.CASCADE)  # 个人用户
    applyJob = models.ForeignKey(Job, on_delete=models.CASCADE)  # 职位
    applyTime = models.DateTimeField(auto_now_add=True)  # 投递简历时间
    applyState = models.NullBooleanField()               # 简历状态 null: 未处理, True: 通过, False: 未通过.

    def __str__(self):
        return self.applyPer.PerInfo.perName + '-' + self.applyJob.jobName