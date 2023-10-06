import math

class HinhHoc:

    def __init__(self, canh: float) -> None:
        self.__canh = canh

    def TinhDienTich(self) -> float:
        pass

class HinhTron(HinhHoc):

    def __init__(self, bankinh: float) -> None:
        super().__init__(bankinh)

    def TinhDienTich(self) -> float:
        return math.pi * self._HinhHoc__canh**2

    def xuat(self):
        print("Bán kính:", self._HinhHoc__canh)
        print("Diện tích hình tròn:", self.TinhDienTich())

ht = HinhTron(5)
ht.xuat()
