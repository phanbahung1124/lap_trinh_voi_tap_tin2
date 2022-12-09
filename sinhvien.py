from Student import SinhVien
def main():
    sv = [SinhVien('Pham Nhat Huy',2004,10),SinhVien('Phan Ba Hung',2004,11),SinhVien('Le Nguyen Vu Duy',2004,8.0),SinhVien('Phan Nam Ha',2004,7.0),SinhVien('Tran Huu Bao Anh',2004,9.0),SinhVien('Nguyen Nhat Minh',2004,8.5)]
    for item in sv:
        print(item)

if __name__ =='__main__':
    main()