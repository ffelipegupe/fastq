var total;
// if user changes value in field
$('.field').change(function() {
  // maybe update the total here?
}).trigger('change');

$('.add').click(function() {
  var target = $('.field', this.parentNode)[0];
  target.value = +target.value + 1;
});

$('.sub').click(function() {
  var target = $('.field', this.parentNode)[0];
  if (target.value > 0) {
    target.value = +target.value - 1;
  }
});
