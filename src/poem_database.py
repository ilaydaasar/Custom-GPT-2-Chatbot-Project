# src/poem_database.py
class PoemDatabase:
    def __init__(self):
        self.poem_database = {
            "winter": {
                "title": "Winter's Embrace",
                "content": """White blankets the fields, a silent hush,
The cold wind whispers with a gentle rush.
Bare branches reach for the pale, silver moon,
And sleeping nature waits for the sun's return, so soon."""
            },
            "nature": {
                "title": "Nature's Song", 
                "content": """The trees are dancing in the breeze so light,
The river flows with all its might.
Birds are singing their morning tune,
Under the golden afternoon."""
            }
        }
    
    def get_poem(self, poem_type="winter"):
        poem_data = self.poem_database.get(poem_type, self.poem_database["winter"])
        return f"{poem_data['title']}\n\n{poem_data['content']}"
    
    def detect_poem_type(self, user_input):
        user_lower = user_input.lower()
        if any(word in user_lower for word in ['winter', 'snow', 'cold']):
            return "winter"
        elif any(word in user_lower for word in ['nature', 'tree', 'river']):
            return "nature"
        else:
            import random
            return random.choice(list(self.poem_database.keys()))