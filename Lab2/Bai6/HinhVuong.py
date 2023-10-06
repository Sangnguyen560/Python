from HinhChuNhat import HinhChuNhat


class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float):
        super().__init__(canh)

    def HinhVuong(self, canh: float):
        pass

    def TinhDienTich(self) -> float:
        return super().TinhDienTich()

    def xuat(self):
        print(f"hinh vuong co canh: {self._canh}")
