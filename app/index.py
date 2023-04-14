from app import app, dao, login, controllers, admin

app.add_url_rule("/", 'index', controllers.home)
app.add_url_rule("/dat_phong", 'book_room', controllers.book_room, methods=["post", "get"])
app.add_url_rule("/login", 'login-my-user', controllers.login_my_user, methods=['get', 'post'])
app.add_url_rule("/logout", 'logout-my-user', controllers.logout_my_user)
app.add_url_rule("/api/get_ca_hoc/<int:ca_hoc_id>", "get-ca-hoc", controllers.get_ca_hoc, methods=['post'])
app.add_url_rule("/api/save_book_room", "save-book-room", controllers.save_book_room, methods=['post'])
app.add_url_rule("/xem_phieu_muon", 'xem_phieu_muon', controllers.xem_phieu_muon)

# login người dùng tại đây
@login.user_loader
def load_user(user_id):
    return dao.get_tai_khoan_by_id(user_id)


# Chạy trang web
if __name__ == '__main__':
    app.run(debug=True)
    # Cờ debug bật để kiểm tra lỗi, triển khai lên sever phải tắt đi
