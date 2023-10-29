import google.generativeai as palm

# Configure PaLM API 
palm.configure(api_key="YOUR_API_KEY")
model = "models/chat-bison-001" 

class ChatBot:
    def __init__(self):
        self.conversation = []
        
    def chat(self, message):
        # Add user message to conversation history
        self.conversation.append({"author": "user", "content": message})
        
        # Generate response 
        response = palm.chat(
            model=model,
            messages=self.conversation,
            candidate_count=3
        ).candidates
        
        # Pick first candidate response
        bot_message = response[0]["content"]
        
        # Add bot message to conversation history
        self.conversation.append({"author": "bot", "content": bot_message})
        
        print("Bot:", bot_message)
        
bot = ChatBot()

while True:
    message = input("You: ")
    if message == "quit":
        break
        
    bot.chat(message)
