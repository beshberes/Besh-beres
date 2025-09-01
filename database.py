import sqlite3
import json
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="besh_beres.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
    
    def create_tables(self):
        """ایجاد جداول مورد نیاز"""
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS knowledge (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT UNIQUE,
                answer TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                usage_count INTEGER DEFAULT 0
            )
        ''')
        
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS conversation_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT,
                ai_response TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def save_knowledge(self, question, answer):
        """ذخیره دانش جدید"""
        try:
            self.conn.execute(
                'INSERT OR REPLACE INTO knowledge (question, answer) VALUES (?, ?)',
                (question, answer)
            )
            self.conn.commit()
        except Exception as e:
            print(f"خطا در ذخیره دانش: {e}")
    
    def load_knowledge(self):
        """بارگذاری دانش از دیتابیس"""
        knowledge = {}
        try:
            cursor = self.conn.execute('SELECT question, answer FROM knowledge')
            for row in cursor:
                knowledge[row[0]] = row[1]
        except Exception as e:
            print(f"خطا در بارگذاری دانش: {e}")
        return knowledge