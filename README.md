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

Ảnh sau khi được đọc sẽ được copy vào database, đồng thời thêm các vector, label và name vào dữ liệu lưu sẵn.
`python re_train`
<br>

### Chạy face recognition
`python recognize_video.py`
hoặc 
`recognize_videos_svm.py`
