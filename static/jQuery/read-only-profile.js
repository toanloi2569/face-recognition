
$(document).ready(function(){
    $('div.form-group :input').prop('readonly', true).css("background-color","transparent");
    $('div.form-group > .custom-select').attr("disabled", true);
    $('#edit-profile').click(function(){
        $('#edit-profile').hide()
        $('#update-profile').show()
        $('div.form-group :input').prop('readonly', false).css("background-color","transparent");
        $('div.form-group > .custom-select').attr("disabled", false);
        swal("Mời cập nhật thông tin");
    });
})