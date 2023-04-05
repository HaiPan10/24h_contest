import hashlib
from datetime import datetime

from app import db, app
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime, Float, Enum, Text, Boolean
from enum import Enum as UserEnum, Enum as StatusEnum, Enum as DayInWeekEnum
from flask_login import UserMixin


# Tat ca cac model deu phai ke thua db.Model
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class GiangVien(BaseModel):
    ho_gv = Column(String(50), nullable=True)
    ten_gv = Column(String(50), nullable=True)
    gioi_tinh = Column(String(15), nullable=True)
    day = relationship('Day', backref='giang_vien', lazy=True)


class PhongHoc(BaseModel):
    ten_phong = Column(String(15), nullable=False)
    kich_co = Column(Integer, nullable=False)
    tinh_trang = Column(String(25), default="Tot")
    lop_hoc = relationship('LopHoc', backref='phong_hoc', lazy=True)
    phieu_muon_phong = relationship('PhieuMuonPhong', backref='phong_hoc', lazy=True)


class CaHoc(BaseModel):
    ten_ca = Column(String(15), nullable=False)
    gio_bat_dau = Column(DateTime)
    gio_ket_thuc = Column(DateTime)
    lop_hoc = relationship('LopHoc', backref='ca', lazy=True)
    phieu_muon = relationship('PhieuMuonPhong', backref='ca', lazy=True)


class TaiKhoan(BaseModel):
    dai_dien_to_chuc = Column(String(50), nullable=False)
    hoTen = Column(String(50), nullable=False)
    gmail = Column(String(50), nullable=True)
    mat_khau = Column(String(50), nullable=False)
    so_luot = Column(Integer, default=1)
    loai_tai_khoan = Column(String(50), nullable=False)
    mssv = Column(String(10), nullable=False)
    da_bi_khoa = Column(Boolean, default=False)
    phieu_muon = relationship('PhieuMuonPhong', backref='tai_khoan', lazy=True)


class MonHoc(BaseModel):
    ten_mon = Column(String(50), nullable=False)
    lop_hoc = relationship('LopHoc', backref='mon_hoc', lazy=True)


class DayInWeek(DayInWeekEnum):
    MON = 1
    TUE = 2
    WED = 3
    THUR = 4
    FRI = 5
    SAT = 6
    SUN = 7


class LopHoc(BaseModel):
    thu_trong_tuan = Column(Enum(DayInWeek))
    mon_hoc_id = Column(Integer, ForeignKey(MonHoc.id), nullable=False)
    ca_id = Column(Integer, ForeignKey(CaHoc.id), nullable=False)
    phong_hoc_id = Column(Integer, ForeignKey(PhongHoc.id), nullable=False)
    day = relationship('Day', backref="lop_hoc", lazy=True)


class Day(BaseModel):
    gv_id = Column(Integer, ForeignKey(GiangVien.id), nullable=False)
    lop_hoc_id = Column(Integer, ForeignKey(LopHoc.id), nullable=False)


class PhieuMuonPhong(BaseModel):
    thoi_gian_dat = Column(DateTime)
    ngay_muon = Column(DateTime)
    ly_do = Column(Text)
    tai_khoan_id = Column(Integer, ForeignKey(TaiKhoan.id), nullable=False)
    ca_id = Column(Integer, ForeignKey(CaHoc.id), nullable=False)
    phong_hoc_id = Column(Integer, ForeignKey(PhongHoc.id), nullable=False)


'''
___________________________________Old code___________________________________
___________________________________Please Don't_______________________________
___________________________________Remove Or Comment__________________________
'''


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class Categories(BaseModel):
    category_name = Column(String(50), nullable=False)
    books = relationship('Books', backref='categories', lazy=True)
    descriptions = Column(Text)
    image = Column(String(250))

    def __str__(self):
        return self.category_name


class Books(BaseModel):
    book_name = Column(String(150), nullable=False)
    author_name = Column(String(100))
    quantity = Column(Integer, default=0)
    import_date = Column(DateTime)
    unit_price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey(Categories.id), nullable=False)
    order_details = relationship('OrderDetails', backref='books', lazy=True)
    sold_numbers = Column(Integer, default=0)
    image = Column(String(250), nullable=False)
    descriptions = Column(Text)
    comments = relationship('Comment', backref='books', lazy=True)

    def __str__(self):
        return self.book_name


class Status(StatusEnum):
    DA_THANH_TOAN = 1
    DANG_GIAO = 2
    CHUA_THANH_TOAN = 3

    def __str__(self):
        if self is Status.DA_THANH_TOAN:
            return "Đã thanh toán"
        elif self is Status.DANG_GIAO:
            return "Đang giao"
        else:
            return "Chưa thanh toán"


class UserAccount(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(250), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    phone_number = Column(String(10), nullable=True, unique=True)
    orders = relationship('Orders', backref='user_account', lazy=True)
    comments = relationship('Comment', backref='user_account', lazy=True)

    def __str__(self):
        return self.name


class Orders(BaseModel):
    order_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey(UserAccount.id), nullable=False)
    order_details = relationship('OrderDetails', backref='orders', lazy=True)
    address = Column(String(250), nullable=True)
    status = Column(Enum(Status), default=Status.CHUA_THANH_TOAN)


class OrderDetails(BaseModel):
    quantity = Column(Integer, default=1)
    unit_price = Column(Float, default=0)
    order_id = Column(Integer, ForeignKey(Orders.id), nullable=False)
    book_id = Column(Integer, ForeignKey(Books.id), nullable=False)


class Comment(BaseModel):
    content = Column(String(255), nullable=False)
    created_date = Column(DateTime, default=datetime.now())
    user_account_id = Column(Integer, ForeignKey(UserAccount.id), nullable=False)
    book_id = Column(Integer, ForeignKey(Books.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        pass
        # db.drop_all()
        # db.create_all()
        # name = 'Admin'
        # username = 'admin'
        # password = str(hashlib.md5('1'.encode('utf-8')).hexdigest())
        # avatar = 'https://res.cloudinary.com/dxjkpbzmo/image/upload/v1669562707/user_admin-removebg-preview_xtqp2h.png'
        # user = UserAccount(name=name, username=username, password=password, avatar=avatar, user_role=UserRole.ADMIN)
        # db.session.add(user)
        # db.session.commit()
        # db.drop_all()
