from HinhHoc import HinhHoc


class HinhChuNhat(HinhHoc):
    def __init__(self, ChieuDai: float, ChieuRong: float):
        self.__chieuDai = ChieuDai
        self.__chieuRong = ChieuRong
        __rong: float

    def HinhChuNhat(self, dai: float, rong: float):
        pass

    def TinhDienTich(self) -> float:
        return self.__chieuDai * self.__chieuRong

    def xuat(self):
        print(
            f"Chieu dai: {self.__chieuDai}, Chieu Rong: {self.__chieuRong}, dien tich HCN: {self.TinhDienTich()}")
