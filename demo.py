# demo.py
from src.chat_bot import ChatBot

def main():
    print("🤖 GPT-2  Chatbot Demo")
    print("=" * 30)
    
    bot = ChatBot()
    
    print("Bot: Merhaba! Sohbet etmeye hazırım. 'quit' yazarak çıkabilirsiniz.")
    
    while True:
        user_input = input("\n👤 User: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("🤖 Bot: Bye! 👋")
            break
        
        response = bot.get_response(user_input)
        print(f"🤖 Bot: {response}")

if __name__ == "__main__":
    main()