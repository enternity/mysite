# (Yên tâm không hại máy tính mày đâu)
# - Cài đặt git trên windows:
- Bước 1: vào trang [git](https://git-scm.com/download/win), đợi nó down về thôi.
- Bước 2: Cứ next là xong :D.
# - Cài đặt python3.8 trên windows:
- Bước 1: vào trang [python.com](https://www.python.org/downloads/)
- Bước 2: download về thôi
- Bước 3: setup, cứ next cho tới gặp cái hình này [![N|solid](https://docs.python.org/3/_images/win_installer.png)
- Bước 4: click vào "Add Python3.x to PATH" xong mới click "Install now"
### - Thế là xong phần cài đặt các thứ cần thiết rồi đấy, easy nhờ =))

# Do somthing with python:
- Tải pip(cái này dài dòng nên muốn thì coi trên mạng, khong để t teamview setup môi trường cho)(mày cài được thì xem như m hay)
- Tải django(framework cho back-end) syntax: pip3 install django==3.0
- Tải thêm cái package env(quản lý môi trường)(không cần thiết lắm)
- Rồi xong phần setup với python,
- VÃ MỒ HỒI CHƯA TA :3
# Do something with git:
- Ở múc độ cơ bản thì git dùng để quản lí source có 3 chức năng chính là: add, commit, push.
- Đầu tiên tất nhiên ta cần down project về chứ nhỉ :D
- Vào [link](https://github.com/enternity/mysite.git) này. Thấy gì không đó là nơi source code của project ấy.
- Giờ clone project về thôi
- Trở ra destop
- Nhấn chuột phải + click vào git bash here á.
- Gõ: git clone https://github.com/enternity/mysite.git
- Gõ: git checkout dev
- Thấy thư muc nào hiện ngoài desktop chưa. Đó là thư mục chứa source code project đấy. (Ảo chưa, cần gì lên trình duyệt tải, magic!!!!)
- Tới đây đã là thành công lớn rồi.
## Chắc m choáng rồi nhờ. M đang nghĩ what the f * c * am i doing? 
## Thôi thì ráng, người lớn mà =)), master cái git này là trùm lắm rồi :V
## Có issue gì cứ raise lên ha, cái tao đang viết mai giờ gọi là markdown, ảo chưa, cứ như html nhờ :v

# Làm việc với github:
Git là nơi mày viết mấy câu lệnh loằn ngà loằn ngoằn còn github là nơi chứa source code của m
- Quy trình nôm na là thế này:
    - Lưu lại source code m viết, trên bash gõ: ```git stautus``` lệnh này có nghĩa là kiểm tra xem m đã thay đổi những file gì nó sẽ hiện lên.
    - Nếu đã ok rồi, thì gõ ```git add .``` lệnh này có nghĩa là lưu lại tất cả những thay đổi m làm.
    - Sau đó, ```git commit -m"[Message]"```: message ở đây m muốn viết gì cũng được. Lệnh này có nghĩa là m đã thay đổi gì trong project để t còn biết. Không cần đọc source code chỉ cần đọc commit là hiểu m làm gì. Example: ```git commit -m"[done]thêm thanh tìm kiếm ở home page"```
    - Sau đó, để tống lên server chỉ cần ```git push```. :D
- Thêm về git:
    - Có những lúc t viết xong push lên, m cần phải lấy code mới về trước khi làm việc thì gõ ```git fetch```, sau đó ```git pull``` là xong. Có những trường hợp xảy ra khác nữa nhưng khi gặp rồi t giải thích rồi hướng dẫn luôn cho khỏi mắc công.
    - Nếu định làm developer thì cái này cần phải học.(Điểm cộng cực to trong măt HR nghe đồn thế hihi).
# Làm việc với bash:
- Chắc m chưa quen với việc dùng BASH, t cũng thế lần đầu gõ lệnh thấy không quen gì cả, click chuột không nhanh hơn à. Không click chuột lâu hơn  nếu xét về mặt thời gian xử lí của máy tính :D
- Vd m muốn copy 1 đoạn nào đấy thì lấy con chuột yêu thích của mọi người xong rồi bold đen như bình thường, thay vì ```Ctrl + C```, thì nhấn ```Ctrl + Shift + C```
- Còn muốn dán thì thay vì ```Ctrl + V``` thì ```Shift + phím Insert```
- Với lại m cũng không cần gõ đúng hết. Ví dụ m gõ ```git com``` thì nhấn thêm nút ```tab``` là xong. Cái này gọi là nhắc lệnh cho nhanh.
- Series làm quen với bash với git hôm nay ít thôi, chứ ngộp :D.
