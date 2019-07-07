from django.contrib import admin
from .models import PerUser, PerEdu, PerExpected, PerInfo, PerWorkExp, ApplyList, CompInfo, CompUser, Job

# Register your models here.

admin.site.register(Job)

# 刘 7/7
from .models import Question, Answer
admin.site.register(Question)
admin.site.register(Answer)

class CompInfoInline(admin.StackedInline):
    model = CompInfo

class JobInline(admin.StackedInline):
    model = Job
    extra = 1

class CompUserAdmin(admin.ModelAdmin):
    inlines = [CompInfoInline, JobInline]

admin.site.register(CompUser, CompUserAdmin)



admin.site.register(ApplyList)


class PerEduInline(admin.StackedInline):
    model = PerEdu

class PerExpectedInline(admin.StackedInline):
    model = PerExpected

class PerInfoInline(admin.StackedInline):
    model = PerInfo

class PerWorkExpInline(admin.StackedInline):
    model = PerWorkExp
    extra = 1

class PerUserAdmin(admin.ModelAdmin):
    inlines = [PerInfoInline, PerEduInline, PerWorkExpInline, PerExpectedInline]

admin.site.register(PerUser, PerUserAdmin)