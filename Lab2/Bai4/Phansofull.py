class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self) -> str:
        return "{}/{}".format(self.tu, self.mau)

    @staticmethod
    def __TimUCLN(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def __TimBCNN(a, b):
        return a * b // PhanSo.__TimUCLN(a, b)

    def __ln__(self, other):
        lps = PhanSo.__TimBCNN(self.mau, other.mau)
        
        self_scaled = self.tu * (lps // self.mau)
        other_scaled = other.tu * (lps // other.mau)
        
        return self_scaled < other_scaled

    def __nn__(self, other):

        lps = PhanSo.__TimBCNN(self.mau, other.mau)
        
        self_scaled = self.tu * (lps // self.mau)
        other_scaled = other.tu * (lps // other.mau)
        
        return self_scaled > other_scaled
    
    def RutGon(self):
        ucln = self.__TimUCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.RutGon()
        return kq
    
    

class DanhSachPhanSo():
    def __init__(self):
        self.dsps = []

    def ThemPhanSo(self, ps: PhanSo):
        self.dsps.append(ps)

    def xuat(self):
        for ps in self.dsps:
            print(ps)

    def PhanBietTuAm(self):
        for index, ps in enumerate(self.dsps):
            if ps.tu < 0 or ps.mau < 0:
                return ps
            
    #1. Đếm số phân số âm trong mảng
    def DemPhanSo(self):
        count = 0
        for ps in self.dsps:
            if ps.tu < 0:
                count += 1
        print("Số phân số âm trong mảng là:", count)
    
    #2. Tìm phân số dương nhỏ nhất
    def TimPhanSoDuongNhoNhat(self):
        vitri = [ps for ps in self.dsps if ps.tu > 0]

        if not vitri:
            print("Không có phân số dương trong mảng.")
            return None

        smallest = min(vitri, key=lambda x: (x.tu, x.mau))
        print("Phân số dương nhỏ nhất là:", smallest)

    #3. Tìm tất cả vị trí của phân số x trong mảng
    def TimViTriPhanSo(self, x: PhanSo):
        vitri = []

        for index, ps in enumerate(self.dsps):
            if ps.tu == x.tu and ps.mau == x.mau:
                vitri.append(index+1)

        if vitri:
            print("Phân số", x, "được tìm thấy tại các vị trí:", vitri)
        else:
            print("Phân số", x, "không có trong mảng.")
    
    #4. Tổng tất cả các phân số âm trong mảng
    def TongPhanSoAm(self):
        TongSoAm = PhanSo()

        for ps in self.dsps:
            if ps.tu < 0 or ps.mau < 0:
                TongSoAm += ps
        return TongSoAm
    
    #5. Xóa phân số x trong mảng
    def XoaPhanSo(self, ps: PhanSo):
        if ps in self.dsps:
            self.dsps.remove(ps)
        else:
            print(f"Phân số {ps} không tồn tại trong mảng.")
    
    #6. Xóa tất cả phân số có tử là x
    def XoaPhanSoTheoTu(self, x):
        self.dsps = [ps for ps in self.dsps if ps.tu != x]

    #7. Sắp xếp phân số theo chiều tăng, giảm; tăng theo mẫu, tử, giảm theo mẫu tử.
    def SapXepTangTrenTu(self):
        self.dsps.sort(key=lambda ps: ps.tu)

    def SapXepGiamTrenTu(self):
        self.dsps.sort(key=lambda ps: ps.tu, reverse=True)

    def SapXepTangTrenMau(self):
        self.dsps.sort(key=lambda ps: ps.mau)

    def SapXepGiamTrenMau(self):
        self.dsps.sort(key=lambda ps: ps.mau, reverse=True)


ps0 = PhanSo(6,9)
ps1 = PhanSo(2,3)
ps2 = PhanSo(1, 6)
ps3 = PhanSo(-6, 8)
ps4 = PhanSo(-3, 8)
ps5 = PhanSo(9, 8)
ps6 = PhanSo(5, -9)
ps7 = PhanSo(4, -8)


dsps = DanhSachPhanSo()
dsps.ThemPhanSo(ps0)
dsps.ThemPhanSo(ps1)
dsps.ThemPhanSo(ps2)
dsps.ThemPhanSo(ps3)
dsps.ThemPhanSo(ps4)
dsps.ThemPhanSo(ps5)
dsps.ThemPhanSo(ps6)
dsps.ThemPhanSo(ps7)
dsps.xuat()
dsps.DemPhanSo()
dsps.TimPhanSoDuongNhoNhat()

x= PhanSo(1,6)
dsps.TimViTriPhanSo(x)

TongSoAm= dsps.TongPhanSoAm()
print("Tổng tử số của các phân số âm trong mảng:", TongSoAm)

print("Xóa phân số ps5 khỏi mảng:")
dsps.XoaPhanSo(ps5)
dsps.xuat()

x = 1 #nhập tử cần xóa
print(f"Xóa tất cả các phân số có tử số bằng {x}:")
dsps.XoaPhanSoTheoTu(x)
dsps.xuat()

print("Sắp xếp tăng theo tử số:")
dsps.SapXepTangTrenTu()
dsps.xuat()

print("Sắp xếp giảm theo tử số:")
dsps.SapXepGiamTrenTu()
dsps.xuat()

print("Sắp xếp tăng theo mẫu số:")
dsps.SapXepTangTrenMau()
dsps.xuat()

print("Sắp xếp giảm theo mẫu số:")
dsps.SapXepGiamTrenMau()
dsps.xuat()


