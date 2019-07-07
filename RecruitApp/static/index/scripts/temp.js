
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


function showimg(num) {
    if (num == 1){
        $("#picture").attr("src", "../../static/index/images/it_pic.png")
    }
    else if (num == 2){
        $("#picture").attr("src", "../../static/index/images/zhizao_pic.png")
    }
    else if (num == 3){
        $("#picture").attr("src", "../../static/index/images/jinrong_pic.png")
    }
    else if(num == 4){
        $("#picture").attr("src", "../../static/index/images/fangdichan_pic.png")
    }
    else if(num == 5){
        $("#picture").attr("src", "../../static/index/images/xiaofei_pic.png")
    }
    else if(num == 6){
        $("#picture").attr("src", "../../static/index/images/fuwu_pic.png")
    }
}

// 返回投递成功与否信息
$(document).ready(function(){
    $('#appAll').bind('click',function(){
        // 获取选中项的id
        inputJobIdList = [];
        $("input[name=hotJobs]").each(function(){
            if($(this).prop('checked'))
                inputJobIdList.append(this.id);
        })
        // 发送ajax请求
        $.ajax({
            async: true,
            url: '/apply/applyCheckedJobs/',
            type: 'post',
            headers: {"X-CSRFToken":$.cookie('csrftoken')},
            data: { // 提交数据
                "inputUserId": inputUserId,
                "inputJobIdList": inputJobIdList,
            },
            success: function(data){
                if(data == 'True'){
                    $('#msg').html('<font color="green">投递成功！</font>')
                }else{
                    $('#msg').html('<font color="brown">投递失败！</font>')
                    }
                }
            });
    });
    $('#appAll').focus(function(){
        $('#msg').html('')
    });
});

$(function(){
    //全选和全不选
    $('#ckAll').bind('click',function(){
        if(this.checked){    //全选
            $("input[name=hotJobs]").each(function(){
                $(this).prop('checked',true);
            })
            $('#appAll').prop("disabled",false);
        }
        else{    //全不选
            $("input[name=hotJobs]").each(function(){
                $(this).prop('checked',false);
            })
            $('#appAll').prop("disabled",true);
        }
    });
    //所有的子项选中或者不全选中后，全选按钮也选中或者不选中
    var allLength=$("input[name=hotJobs]").length; //所有的checkbox的长度
    $("input[name=hotJobs]").each(function(){
        $(this).bind('click',function(){
            var selectedLength=$("input[name=hotJobs]:checked").length;//所有的选中的checkbox的长度
            if(selectedLength==allLength){
                $('#ckAll').prop("checked",true);//全选按钮
            }
            else{
                $('#ckAll').prop("checked",false);
            }
            if(selectedLength==0){
                $('#appAll').prop("disabled",true);
            }
            else{
                $('#appAll').prop("disabled",false);
            }
        })
        
    })
})

$(document).ready(function () {
    catalog = $("#selectBox").val();
    if (catalog == 'company') {
        $("#inputBox").attr('placeholder', '请输入公司名称或关键词，如华为、联想等')
    }
    else {
        $("#inputBox").attr('placeholder', '请输入关键词，如JAVA，销售等')
    }
})