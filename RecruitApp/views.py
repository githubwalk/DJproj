from django.shortcuts import render

# Create your views here.

# 07/06 11:33 add by 黄涣升

#主页
def index(request, currentCity):
    '''
    Get_input: currentCity;
    return: 
    '''
    return render(request, 'index.html', {'currentCity': currentCity })
# end