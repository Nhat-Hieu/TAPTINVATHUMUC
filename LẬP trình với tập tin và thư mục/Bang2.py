###Mở 1 tập tin văn bản (đường dẫn và tên file do bạn tự xác định) để đọc
f1 = open('D:/data/My Documents/test.txt', mode = 'r')

###Mở 1 tập tin văn bản (đường dẫn và tên file do bạn tự xác định) để ghi
f2 = open('D:/data/My Documents/test.txt', mode = 'w')

###Mở 1 tập tin nhị phân (đường dẫn và tên file do bạn tự xác định; có thể chọn 1 file ảnh) để đọc và ghi
f3 = open('D:/data/My Documents/Gun.jpg', mode = 'r+')

###Mở 1 tập tin văn bản để đọc, biết các kí tự của tập tin này tuân theo chuẩn Unicode – UTF-8
f4 = open('D:/data/My Documents/Filenaydetest.txt', mode = 'r', encoding = 'utf-8')

###Thao tác đóng tập tin
f1.close()
f2.close()
f3.close()
f4.close()

###Mở tập tin văn bản để đọc bằng cấu trúc câu lệnh
try:
    f5 = open("D:/data/My Documents/Filenaydetest.txt", mode = 'r')
finally:
    file5.close()

###Mở tập tin văn bản để đọc bằng cấu trúc:
with open("D:/data/My Documents/Filenaydetest.txt", mode = 'r' , encoding = 'utf-8') as f: f.read()

###Mở tập tin văn bản Unicode và ghi vào 3 dòng có nội dung tùy ý bạn
with open("D:/data/My Documents/Filenaydetest.txt", mode = 'a') as Filenaydetest:
    Filenaydetest.write("Good night!")
    Filenaydetest.write("Xin chao!")
    Filenaydetest.write("Good bye!")

###Mở tập tin văn bản Unicode, đọc toàn bộ nội dung của văn bản và in ra màn hình
f6 = open('D:/data/My Documents/Filenaydetest.txt', mode = 'r')
read_all = f6.read()
print(read_all)

###Mở tập tin nhị phân (chọn 1 bức ảnh),đọc và ghi toàn bộ nội dung tập tin ra màn hình.
f7 = open('D:/data/My Documents/Gun.jpg', mode = 'r+')
read_write_all= f7.read()
print(read_write_all)