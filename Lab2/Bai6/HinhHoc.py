import math


class HinhHoc:
    def __init__(self, canh: float) -> None:
        self._canh = canh

    def tinhDienTich(self) -> float:
        return self._canh * self._canh * math.pi

    def xuat(self):
        print(
            f"Hình học có cạnh: {self._canh}, diện tích là: {self.tinhDienTich()}")


if __name__ == "__main__":
    hh = HinhHoc(5)
    hh.xuat()
