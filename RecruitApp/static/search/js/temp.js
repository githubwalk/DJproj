var flag = 0;
var TempCity='';
var TempWork=0;
var TempMoney=0;
var TempYear=0;
var TempStudy=0;

function SelectCity(id) {
    if (flag == 0) {
        document.getElementById(id).style.display = 'block';
        flag = 1;
    }
    else {
        document.getElementById(id).style.display = 'none';
        flag = 0;
    }
}

function ChangeCity(ChildFlag) {
    var list = document.getElementsByTagName('button1');
    for (let i = 0; i < list.length; i++) {
        list[i].removeAttribute('class');
    }
    ChildFlag.setAttribute('class', 'checked');
    document.getElementById('CityFather').innerHTML = ChildFlag.innerHTML;
    TempCity=ChildFlag.id;
    
    window.location.href = '/RecruitApp/search/'+'?'+'location='+TempCity+'&profession='+TempWork+'&salary='+TempMoney+'&experience='+TempYear+'&education='+TempStudy;
}
function ChangeWork(WorkFlag) {
    var list = document.getElementsByTagName('button2');
    for (let i = 0; i < list.length; i++) {
        list[i].removeAttribute('class');
    }
    WorkFlag.setAttribute('class', 'checked');
    TempWork=WorkFlag.id;
    window.location.href = '/RecruitApp/search/'+'?'+'location='+TempCity+'&profession='+TempWork+'&salary='+TempMoney+'&experience='+TempYear+'&education='+TempStudy;
}
function ChangeMoney(MoneyFlag) {
    var list = document.getElementsByTagName('button3');
    for (let i = 0; i < list.length; i++) {
        list[i].removeAttribute('class');
    }
    MoneyFlag.setAttribute('class', 'checked');
    TempMoney=MoneyFlag.id;
    window.location.href = '/RecruitApp/search/'+'?'+'location='+TempCity+'&profession='+TempWork+'&salary='+TempMoney+'&experience='+TempYear+'&education='+TempStudy;
}

function ChangeYear(YearFlag) {
    var list = document.getElementsByTagName('button4');
    for (let i = 0; i < list.length; i++) {
        list[i].removeAttribute('class');
    }
    YearFlag.setAttribute('class', 'checked');
    TempYear=YearFlag.id;
    window.location.href = '/RecruitApp/search/'+'?'+'location='+TempCity+'&profession='+TempWork+'&salary='+TempMoney+'&experience='+TempYear+'&education='+TempStudy;
}
function ChangeStudy(StudyFlag) {
    var list = document.getElementsByTagName('button5');
    for (let i = 0; i < list.length; i++) {
        list[i].removeAttribute('class');
    }
    StudyFlag.setAttribute('class', 'checked');
    TempStudy=StudyFlag.id;
    window.location.href = '/RecruitApp/search/'+'?'+'location='+TempCity+'&profession='+TempWork+'&salary='+TempMoney+'&experience='+TempYear+'&education='+TempStudy;
}


