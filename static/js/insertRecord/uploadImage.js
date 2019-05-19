function readURL1(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#anh1').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
};

$("#anh_chan_dung").change(function () {
  readURL1(this);
});

function readURL2(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#anh2').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
};

$("#anh_cmt_truoc").change(function () {
  readURL2(this);
});
function readURL3(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#anh3').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
};

$("#anh_cmt_sau").change(function () {
  readURL3(this);
});