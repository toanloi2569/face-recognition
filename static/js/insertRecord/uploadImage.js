function readURL1(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    console.log(('Loi'));
    
    reader.onload = function (e) {
      $('#anh1').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
};

$("#anh_chan_dung").change(function () {
  console.log("Van la loi");
  
  readURL1(this);
});