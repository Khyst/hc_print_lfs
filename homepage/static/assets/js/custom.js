$(function() {
  $('body').scroll(function(){
    console.log('현재 스크롤 값은' + $('body').scrollTop());
  })
})(jQuery);

function show_product_content(idx){
  $('.poster_wrap').addClass('d-none')
  $('.poster_wrap').eq(idx-1).removeClass('d-none')
}

function make_query(){
  alert('click');
  $('#query').addClass('d-block');
}

function exit_query(){
  $('#query').removeClass('d-block');
}

function view_mobile_auth(){
  alert('click');

  if($('#mobile_nav').attr('class')=="d-block"){
    $('#mobile_nav').addClass('d-none');  
  }
  else{
    $('#mobile_nav').addClass('d-block');
  }
}

function click_banner_btn(){
  

  if($('.banner_list_lg').hasClass('hided')){
    $('.banner_list_lg').show();
    $('.banner_list_lg').removeClass('hided');

  }
  else{
    $('.banner_list_lg').hide();
    $('.banner_list_lg').addClass('hided');
  }


  // $('.banner_list_lg').show();
}