from app.models import GiangVien, MonHoc, Day, LopHoc, PhongHoc, PhieuMuonPhong, CaHoc, TaiKhoan, Tag
from app import db, app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class GiangVienView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class MonHocView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class CaView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class PhongHocView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class TaiKhoanView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class LopHocView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class DayView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class PhieuMuonPhongView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


class TagView(ModelView):
    can_view_details = True
    can_edit = True
    can_delete = True


admin = Admin(app=app, name='Quản Trị Mượn Đặt Phòng', template_mode='bootstrap4')
admin.add_view(GiangVienView(GiangVien, db.session, name='Giảng viên'))
admin.add_view(MonHocView(MonHoc, db.session, name='Môn học'))
admin.add_view(CaView(CaHoc, db.session, name='Danh sách ca'))
admin.add_view(LopHocView(LopHoc, db.session, name='Lớp học'))
admin.add_view(PhongHocView(PhongHoc, db.session, name='Phòng học'))
admin.add_view(TaiKhoanView(TaiKhoan, db.session, name='Tài khoản'))
admin.add_view(DayView(Day, db.session, name='Danh sách dạy'))
admin.add_view(PhieuMuonPhongView(PhieuMuonPhong, db.session, name='Phiếu mượn phòng'))
admin.add_view(TagView(Tag, db.session, name='Tag'))
