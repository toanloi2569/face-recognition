
/* Loại */
var hanoi =
    '<option selected disabled>Quận/Huyện</option>' +
    '<option value="Quận Ba Đình">Quận Ba Đình</option>' +
    '<option value="Quận Cầu Giấy">Quận Cầu Giấy</option>' +
    '<option value="Quận Đống Đa">Quận Đống Đa</option>' +
    '<option value="Quận Hà Đông">Quận Hà Đông</option>' +
    '<option value="Quận Hai Bà Trưng">Quận Hai Bà Trưng</option>' +
    '<option value="Quận Hoàn Kiếm">Quận Hoàn Kiếm</option>' +
    '<option value="Quận Hoàng Mai">Quận Hoàng Mai</option>' +
    '<option value="Quận Long Biên">Quận Long Biên</option>' +
    '<option value="Quận Tây Hồ">Quận Tây Hồ</option>' +
    '<option value="Quận Thanh Xuân">Quận Thanh Xuân</option>' +
    '<option value="Thị xã Sơn Tây">Thị xã Sơn Tây</option>' +
    '<option value="Huyện Ba Vì">Huyện Ba Vì</option>' +
    '<option value="Huyện Chương Mỹ">Huyện Chương Mỹ</option>' +
    '<option value="Huyện Đan Phượng">Huyện Đan Phượng</option>' +
    '<option value="Huyện Đông Anh">Huyện Đông Anh</option>' +
    '<option value="Huyện Gia Lâm">Huyện Gia Lâm</option>' +
    '<option value="Huyện Hoài Đức">Huyện Hoài Đức</option>' +
    '<option value="Huyện Mê Linh">Huyện Mê Linh</option>' +
    '<option value="Huyện Mỹ Đức">Huyện Mỹ Đức</option>' +
    '<option value="Huyện Phú Xuyên">Huyện Phú Xuyên</option>' +
    '<option value="Huyện Phúc Thọ">Huyện Phúc Thọ</option>' +
    '<option value="Huyện Quốc Oai">Huyện Quốc Oai</option>' +
    '<option value="Huyện Sóc Sơn">Huyện Sóc Sơn</option>' +
    '<option value="Huyện Thạch Thất">Huyện Thạch Thất</option>' +
    '<option value="Huyện Thanh Oai">Huyện Thanh Oai</option>' +
    '<option value="Huyện Thanh Trì">Huyện Thanh Trì</option>' +
    '<option value="Huyện Thường Tín">Huyện Thường Tín</option>' +
    '<option value="Quận Nam Từ Liêm">Quận Nam Từ Liêm</option>' +
    '<option value="Huyện Ứng Hòa">Huyện Ứng Hòa</option>' +
    '<option value="Quận Bắc Từ Liêm">Quận Bắc Từ Liêm</option>';

var hochiminh =
    '<option selected disabled>Quận/Huyện</option>' +
    '<option value="Quận 1">Quận 1</option>' +
    '<option value="Quận 2">Quận 2</option>' +
    '<option value="Quận 3">Quận 3</option>' +
    '<option value="Quận 4">Quận 4</option>' +
    '<option value="Quận 5">Quận 5</option>' +
    '<option value="Quận 6">Quận 6</option>' +
    '<option value="Quận 7">Quận 7</option>' +
    '<option value="Quận 8">Quận 8</option>' +
    '<option value="Quận 9">Quận 9</option>' +
    '<option value="Quận 10">Quận 10</option>' +
    '<option value="Quận 11">Quận 11</option>' +
    '<option value="Quận 12">Quận 12</option>' +
    '<option value="Quận Bình Tân">Quận Bình Tân</option>' +
    '<option value="Quận Bình Thạnh">Quận Bình Thạnh</option>' +
    '<option value="Quận Gò Vấp">Quận Gò Vấp</option>' +
    '<option value="Quận Phú Nhuận">Quận Phú Nhuận</option>' +
    '<option value="Quận Tân Bình">Quận Tân Bình</option>' +
    '<option value="Quận Tân Phú">Quận Tân Phú</option>' +
    '<option value="Quận Thủ Đức">Quận Thủ Đức</option>' +
    '<option value="Huyện Bình Chánh">Huyện Bình Chánh</option>' +
    '<option value="Huyện Cần Giờ">Huyện Cần Giờ</option>' +
    '<option value="Huyện Củ Chi">Huyện Củ Chi</option>' +
    '<option value="Huyện Hóc Môn">Huyện Hóc Môn</option>' +
    '<option value="Huyện Nhà Bè">Huyện Nhà Bè</option>';
var nguyenquan = document.getElementById("tp_nguyen_quan");
nguyenquan.addEventListener("click", function () {
    if (nguyenquan.value === "Hà Nội") {
        render_nguyen_quan(hanoi);
    } else if (nguyenquan.value === "Hồ Chí Minh") {
        render_nguyen_quan(hochiminh);
    } else {
        render_nguyen_quan('<option value="">--Loại--</option>');
    }
});
function render_nguyen_quan(contentLoai) {
    document.getElementById("huyen_nguyen_quan").innerHTML = contentLoai;
};
var thuongtru = document.getElementById("tp_thuong_tru");
thuongtru.addEventListener("click", function () {
    if (thuongtru.value === "Hà Nội") {
        render_thuong_tru(hanoi);
    } else if (thuongtru.value === "Hồ Chí Minh") {
        render_thuong_tru(hochiminh);
    } else {
        render_thuong_tru('<option value="">--Loại--</option>');
    }
});
function render_thuong_tru(contentLoai) {
    document.getElementById("huyen_thuong_tru").innerHTML = contentLoai;
};
var tamtru = document.getElementById("tp_tam_tru");
tamtru.addEventListener("click", function () {
    if (tamtru.value === "Hà Nội") {
        render_tam_tru(hanoi);
    } else if (tamtru.value === "Hồ Chí Minh") {
        render_tam_tru(hochiminh);
    } else {
        render_tam_tru('<option value="">--Loại--</option>');
    }
});
function render_tam_tru(contentLoai) {
    document.getElementById("huyen_tam_tru").innerHTML = contentLoai;
}
