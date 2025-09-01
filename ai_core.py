import nltk
from nltk.tokenize import word_tokenize
import json

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