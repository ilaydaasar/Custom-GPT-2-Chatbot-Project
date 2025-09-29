# src/chat_bot.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from src.text_cleaner import extract_clean_response
from src.jokemanager import JokeManager
from src.poem_database import PoemDatabase

class ChatBot:
    def __init__(self, model_path="models/checkpoint-420"):
        self.model, self.tokenizer, self.device = self.load_model(model_path)
        self.joke_manager = JokeManager()
        self.poem_db = PoemDatabase()
        self.conversation_history = []
        
    def load_model(self, checkpoint_path):
        print("🚀 Model loading...")
        tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
        model = AutoModelForCausalLM.from_pretrained(checkpoint_path)
        
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        return model, tokenizer, device
    
    def get_response(self, user_input):
        # Özel durumlar
        if any(word in user_input.lower() for word in ['poem', 'poetry', 'write a poem']):
            poem_type = self.poem_db.detect_poem_type(user_input)
            return self.poem_db.get_poem(poem_type)
        
        if self.joke_manager.waiting_for_why and user_input.lower() in ['why', 'wht']:
            punchline = self.joke_manager.get_punchline(self.joke_manager.last_joke_type)
            self.joke_manager.waiting_for_why = False
            return punchline
        
        # Konuşma geçmişine ekle
        self.conversation_history.append(f"User: {user_input}")
        
        
        if len(self.conversation_history) >= 2:
            context = "\n".join(self.conversation_history[-4:]) + "\nAssistant:"
        else:
            context = f"User: {user_input}\nAssistant:"
        
        
        inputs = self.tokenizer(
            context, 
            return_tensors="pt",
            padding=True,  # Padding 
            truncation=True,  # Truncation 
            max_length=512  # Maksimum uzunluk
        ).to(self.device)
        
        
        attention_mask = (inputs['input_ids'] != self.tokenizer.pad_token_id).long()
        
        
        generation_config = GenerationConfig(
            max_new_tokens=60,
            min_new_tokens=15,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            top_k=50,
            repetition_penalty=1.2,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs['input_ids'],
                attention_mask=attention_mask,  # ✅ ATTENTION MASK EKLENDİ
                generation_config=generation_config,
                num_return_sequences=1,
            )
            
            raw_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            clean_response = extract_clean_response(raw_response, context)
            
            # Bot yanıtını geçmişe ekle
            self.conversation_history.append(f"Assistant: {clean_response}")
            
            # Konuşma geçmişi çok uzunsa temizle
            if len(self.conversation_history) > 6:
                self.conversation_history = self.conversation_history[-6:]
            
            
            final_response = self.joke_manager.handle_joke_flow(user_input, clean_response)
            
            return final_response