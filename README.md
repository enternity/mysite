# Welcome to back-end with Django
> Sở dĩ t chọn Django làm back-end vì t biết mỗi cái này =))))

# How to woking with Django
1. Bây giờ t với m mới đang làm với mục các bài thì quan tâm thư mục ```article``` thôi.
2. Những file ```html``` thì bỏ trong thư mục ```template``` (bên trong ```article```)
3. Khi mà những chỗ cần ```href, link, source, etc```  mà cần ```css/js``` thì nhớ thêm 
```{% static 'đường dẫn'%}```. Vd ```{% static 'js/sad.js' %}```
4. Đương nhiên tất cả các thư mục ```js, css``` đều nằm trong ```static```
5. Với image cho back-ground thì cũng trong ```static``` luôn.
6. Khi ```routing``` thì phức tạp hơn tí xíu. Nhưng cái này để  sau.

# Welcome to the hell: Github.
1. Trước hết thì workflow của github trước:
[Workflow github](https://res.cloudinary.com/practicaldev/image/fetch/s--M_fHUEqA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/128hsgntnsu9bww0y8sz.png)
> Ghê chưa. Không hiểu cũng chả sao cả :3.

2. Khi mở máy ra code. Trước hết nên lấy code mới nhất từ server về, cho đỡ *Rắc Rối* sau này. Lí do t bôi chữ rắc rối vì nó cả là 1 chủ đề :3. Nói chung muốn ko *Rắc Rối* thì nên mỗi lần làm thì kiểm tra code mình đang làm là mới nhất được lấy trên server về.
    1. Cú pháp: ```git fetch```. Sau đó ```git pull```. Thế là xong.
3. Upload code lên server. Tuần tự các bước như sau:
    1. Mở ```bash``` trong thư mục chứa project ```git status``` (Kiểm tra xem đã thay đổi những gì).
    2. ```git add .```(Lưu ý có dấu chấm sau chữ ```add```).
    3. ```git commit -m "message"```. Với message tùy ý. Quy ước của t với m khi làm xong tính năng gì mà push lên thì thêm ```[done]``` ở trước message. ```[error] nếu cái gì đó lỗi```. ```[modify] ``` là chỉnh sửa file gì đó. Vd  messages như sau: ```[done] homepage.html ```. ```[error] can't load style.css ```, ```[modify] homepage.html```. 
    4. Bước cuối ```git push```
4. *Lưu ý nhỏ*: Nên kiểm tra đang ở nhánh nào trước khi push. Nhưng cái này để t setup trước nên ko cần lo lắng lắm. Kiểm tra đang ở trên branch nào: ```git branch -a```(Nhánh có đánh dấu *).
5. Ví dụ như m làm rối tung rối mù lên, muốn đưa nó về mặc định ban đầu thì tuần tự các bước sau:
    1. ```git status``` kiểm tra xem m đã thay đổi những gì. Vd: nó hiện lên: 
    ```sh
        modify: article/static/main.css
        delete: article/templates/homepage.html
    ```
    2. Lựa những file m muốn đưa về mặc định, vd như muốn đưa về  mặc định file ```main.css``` thì gõ ```git checkout article/static/main.css```. Hoặc muốn đưa về default cả thư mục ```article```
    thì ```git checkout article/```.

# Còn cái bước chạy localhost nữa nhưng để sau. Cái này dễ nên ko sao.
