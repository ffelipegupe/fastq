$input = $('input[type="text"]');

$('.btn').on('click',function(){
     $val = $input.val();
    if ($(this).hasClass('btn-minuse')) {
     $input.val(parseInt($val)-1);
    } else {
    $input.val(parseInt($val)+1);
    }
});

$('.btn2').on('click',function(){
    $val = $input.val();
   if ($(this).hasClass('btn-minuse-2')) {
    $input.val(parseInt($val)-1);
   } else {
   $input.val(parseInt($val)+1);
   }
});
