import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import json
import numpy as np

nltk.download('punkt')

class BeshBeresAI:
    def __init__(self, data_file="memory.json"):
        self.data_file = data_file
        self.knowledge = self.load_memory()
    
    def load_memory(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_memory(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=4)
   
    def ethical_check(self, text):
        banned_words = ["تنفر", "خشونت", "آزار", "نفرت"]
        for word in banned_words:
            if word in text:
                return False
        return True

    def learn(self, question, answer):
        if self.ethical_check(answer):
            self.knowledge[question] = answer
            self.save_memory()
            print("یاد گرفتم! ✅")
        else:
            print("این پاسخ با قوانین اخلاقی ما مغایرت دارد! ❌")
    
    def respond(self, user_input):
        tokens = word_tokenize(user_input)
        for key in self.knowledge:
            if any(word in key for word in tokens):
                return self.knowledge[key]
        return "هنوز یاد نگرفتم. به من یاد بده."

# آزمایش کنید
if __name__ == "__main__":
    ai = BeshBeresAI()
    ai.learn("سلام", "سلام! چطوری؟")
    print(ai.respond("سلام"))

class EnhancedBeshBeresAI:
    def __init__(self, data_file="memory.json"):
        self.data_file = data_file
        self.knowledge = self.load_memory()
        self.stemmer = PorterStemmer()
        self.conversation_history = []
    
    def load_memory(self):
        """بارگذاری حافظه از فایل JSON"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_memory(self):
        """ذخیره حافظه در فایل JSON"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=4)
    
    def preprocess_text(self, text):
        """پردازش پیشرفته متن ورودی با تبدیل به حروف کوچک و ریشه‌یابی"""
        tokens = word_tokenize(text.lower())
        stems = [self.stemmer.stem(token) for token in tokens if token.isalpha()]
        return stems
    
    def learn(self, question, answer):
        """یادگیری پاسخ جدید"""
        self.knowledge[question] = answer
        self.save_memory()
        print("✅ یاد گرفتم!")
    
    def respond(self, user_input):
        """پاسخ به کاربر با استفاده از پردازش پیشرفته متن"""
        # افزودن پیام کاربر به تاریخچه مکالمه
        self.conversation_history.append(f"User: {user_input}")
        
        # پردازش متن ورودی
        tokens = self.preprocess_text(user_input)
        
        # جستجو در دانش موجود
        for key in self.knowledge:
            key_tokens = self.preprocess_text(key)
            if any(token in key_tokens for token in tokens):
                response = self.knowledge[key]
                self.conversation_history.append(f"AI: {response}")
                return response
        
        # اگر پاسخی یافت نشد
        self.conversation_history.append("AI: هنوز یاد نگرفتم")
        return "هنوز یاد نگرفتم. به من یاد بده."
    
    def show_conversation_history(self):
        """نمایش تاریخچه کامل مکالمه"""
        for entry in self.conversation_history:
            print(entry)

# تست سیستم
if __name__ == "__main__":
    ai = EnhancedBeshBeresAI()
    ai.learn("سلام", "سلام! چطوری؟")
    ai.learn("اسم تو چیه؟", "من بش برس هستم!")
    
    print(ai.respond("سلام"))
    print(ai.respond("اسم تو چیست؟"))
    
    ai.show_conversation_history()