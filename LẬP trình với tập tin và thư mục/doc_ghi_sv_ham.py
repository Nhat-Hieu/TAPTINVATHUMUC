from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc:str, ten_tap_tin:str, obj:SinhVien):
    try:
        with open(os.path.join(thumuc, ten_tap_tin), 'wb') as f:
            pickle.dump(obj,f)
        print("Hoàn thành quá trình ghi dữ liệu vào tập tin")
    except Exception as e:
        print("Xảy ra lỗi trong quá trình ghi file")

def doc_sinhvien(thumuc:str, ten_tap_tin:str) -> SinhVien:
    try:
        with open(os.path.join(thumuc, ten_tap_tin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def main():
    path = "D:/data/My Documents/"
    filename ="sinhvien2.dat"
    sv1 = SinhVien("Nhat Hieu", 2004, 10.0)
    ghi_sinhvien(path,filename,sv1)
    noidung = doc_sinhvien(path,filename)
    print(noidung)
    print("Kết thúc chương trình")

if __name__=='__main__':
    main()