# src/jokemanager.py
class JokeManager:
    def __init__(self):
        self.last_joke = ""
        self.last_joke_type = ""
        self.waiting_for_why = False
        
        self.joke_database = {
            "atoms": {
                "setup": "Why don't scientists trust atoms",
                "punchline": "Because they make up everything!"
            },
            "scarecrow": {
                "setup": "Why did the scarecrow win an award",
                "punchline": "Because he was outstanding in his field!"
            }
        }
    
    def detect_joke_type(self, joke_text):
        joke_lower = joke_text.lower()
        if "atom" in joke_lower:
            return "atoms"
        elif "scarecrow" in joke_lower:
            return "scarecrow" 
        else:
            return "atoms"
    
    def get_punchline(self, joke_type):
        return self.joke_database.get(joke_type, {}).get("punchline", "Because that's the punchline!")
    
    def handle_joke_flow(self, user_input, bot_response):
        user_lower = user_input.lower()
        
        if any(word in user_lower for word in ['joke', 'laugh', 'funny']):
            self.last_joke = bot_response
            self.last_joke_type = self.detect_joke_type(bot_response)
            self.waiting_for_why = True
            return bot_response
        
        elif self.waiting_for_why and any(word in user_lower for word in ['why', 'wht']):
            self.waiting_for_why = False
            return self.get_punchline(self.last_joke_type)
        
        else:
            self.waiting_for_why = False
            return bot_response