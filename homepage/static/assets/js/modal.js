$(document).ready(
    function(){
        $('#notice_modal_1').removeClass('fade');
        $('#notice_modal_1').addClass('d-block');

        $('#notice_modal_2').removeClass('fade');
        $('#notice_modal_2').addClass('d-block');
    }
)

function exit_btn(){
    $('#notice_modal_1').addClass('fade');
    $('#notice_modal_1').removeClass('d-block');
    
    $('#notice_modal_2').addClass('fade');
    $('#notice_modal_2').removeClass('d-block');
}