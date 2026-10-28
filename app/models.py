# app/models.py
# ==========================================
# 【Model】データベースの設計図となるファイル
# ==========================================

from app import db
from datetime import datetime

# 1. ユーザーテーブル (users)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

# 2. レシピテーブル (recipes)
class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=False) 
    taste = db.Column(db.String(20))                 
    instructions = db.Column(db.Text)
