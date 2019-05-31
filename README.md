Follow theo tutorial [OpenCV Face Recognition](https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/?fbclid=IwAR04A4zlejp4faM49f3GkJITtKSAQ-ZNtmEH0oAQY6Xs3STGH8cDpTuu4ZA) của Adrian Rosebrock và tutorial [Deep face recognition with Keras, Dlib and OpenCV](https://krasserm.github.io/2018/02/07/deep-face-recognition/) của Martin Krasser

# Sử dụng : 
<br>

### Các phụ thuộc
`pip install cmake`<br>
`pip install -r requirements.txt`<br>
`python down_landmarks.py`<br>
`mkdir database` <br>

### Thêm ảnh vào database:
Tạo 1 folder với tên là tên người trong ảnh, ở trong folder newdatabase <br>
Copy ảnh vào folder vừa được tạo, tên file ảnh nên là tên người trong ảnh.<br>
`python add_img.py`

Ảnh sau khi được đọc sẽ được copy vào database, đồng thời thêm các vector, label và name vào dữ liệu lưu sẵn. <br>
`python re_train`
<br>

### Chạy face recognition
Nhận diện trong videos sử dụng phương pháp phân loại theo khoảng cách vector 
`python recognize_video.py -v [filename]`
Nhận diện trong videos sử dụng phương pháp phân loại theo thuật toán  SVM
`python recognize_video_svm.py -v [filename]`
Nhận diện trong ảnh
`python recognize_img.py -i [filename]`

### Chạy server nhận diện ảnh
`python server.py`
Truy cập vào http://localhost:5000/uploader
