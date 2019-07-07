$(window).scroll(function(event){
    //滚动条高度+视窗高度 = 可见区域底部高度
    // var visibleBottom = window.scrollY + document.documentElement.clientHeight;
    //可见区域顶部高度
    var xians = document.getElementsByClassName('summary-fixed');
    if(window.scrollY>167){
     xians[0].style.display='inline';
    }
    else{
      xians[0].style.display='none';
    }
})
