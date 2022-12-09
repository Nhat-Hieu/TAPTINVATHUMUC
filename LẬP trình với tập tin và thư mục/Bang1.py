###Sử dụng thư viện os
import os


###In ra màn hình thư mục làm việc hiện tại của chương trình
def current_path():
    print('Thư mục hiện tại:', os.getcwd())
    print()
current_path()


###Chuyển đến thư mục: ‘D:/data’, sau đó in thư mục hiện tại ra màn hình
os.chdir('D:/data/')
current_path()


###Tạo thư mục con có tên là ‘nnlt’, sử dụng hàm makedirs()
#Thư mục con
directory = 'nnlt'
#Thư mục mẹ
parent_dir = 'D:/data/'
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)

##Lệt kê tất cả các tập tin và thư mục có trong thư mục ‘My Documents’
path = "D:/data/My Documents/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
#In ra màn hình
print(dir_list)

#Kiểm tra 1 file (tự nhập đường dẫn và tên tập tin gồm cả phần mở rộng) có tồn tại trong máy hay không?
def kiem_tra(path):
    result = os.path.exists(path)
    print(result)
    return result
kiem_tra("D:/data/My Documents")
kiem_tra("D:/data/My Documents/khoqua.txt")

#Xóa 1 thư mục và xóa 1 file trong máy tính
#Xóa 1 file
location = "D:/data/My Documents/"
path = os.path.join(location, "khoqua.txt")
os.remove(path)

#Xóa 1 thư mục
directory = "quakho"
parent = "D:/data/My Documents/"
path = os.path.join(parent, directory)

os.rmdir(path)