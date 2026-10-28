from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQLへの接続設定（rootパスワードは自分の物に変更して使っている、一応）
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/dinner_planner_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 下の行でコントローラーとモデルを読み込む（エラー防止のため最後に書く）
from app import controllers, models
