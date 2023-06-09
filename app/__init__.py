# Khởi tạo packet
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary
from flask_babelex import Babel

# Khởi tạo packet
app = Flask(__name__)
app.secret_key = 'ahdfpiwqeuiqudasdasdncblzbvjlhajz,nfm,sandkqwpuep'

# Cau hinh database trong day
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql12610119:nxBW8kc792@sql12.freemysqlhosting.net' \
                                        '/sql12610119?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
cloudinary.config(
    cloud_name='dxjkpbzmo',
    api_key='728767975167981',
    api_secret='XG9MHhjvkixgZcRfriKwyXSEqjM'
)
db = SQLAlchemy(app=app)
# Khai báo 1 đối tượng login mananger để quản lý login
login = LoginManager(app=app)

# Dịch admin sang tiếng Việt
babel = Babel(app=app)

app.config['FORM_KEY'] = 'form'


@babel.localeselector
def load_locale():
    return 'vi'
