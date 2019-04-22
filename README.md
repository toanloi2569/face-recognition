Follow theo tutorial [OpenCV Face Recognition](https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/?fbclid=IwAR04A4zlejp4faM49f3GkJITtKSAQ-ZNtmEH0oAQY6Xs3STGH8cDpTuu4ZA) của Adrian Rosebrock và tutorial [Deep face recognition with Keras, Dlib and OpenCV](https://krasserm.github.io/2018/02/07/deep-face-recognition/) của Martin Krasser

# Sử dụng : 
<br>

### Các phụ thuộc
`pip install -r requirements.txt`<br>
`python down_landmarks.py`<br>

### Thêm ảnh vào database:
Copy ảnh vào newdatabase, tên file ảnh là tên người trong ảnh.<br>
`python add_img.py`

Ảnh sau khi được đọc sẽ được copy vào database, đồng thời thêm các vector, label và name vào dữ liệu lưu sẵn. Nếu không đọc được ảnh, ảnh vẫn sẽ nằm trong newdatabase
<br>

### Chạy face recognition
`python recognize_video.py`
