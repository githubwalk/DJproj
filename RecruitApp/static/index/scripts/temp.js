

function ProfessionJump(name){
    // 移动到第一栏职位后展开后续浮窗
    window.location.href ='/RecruitApp/index/'+name;

}

function ProfessionShow(id){
    //通过id显示职位栏
    document.getElementById(id).style.display='block';
}

function ProfessionHide(id){
    //通过id隐藏鼠标没移到的职位栏
    document.getElementById(id).style.display='none';
}
