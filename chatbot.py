import re
class SimpleAIChatbot:
    def __init__(self):
        self.qa_pairs = [
            (r'hi|hello|hey', "Hello! How can I assist you today?"),
            (r'how are you', "I'm an AI, so I'm always functioning at optimal performance! How about you?"),
            (r'what is your name', "I'm your friendly AI chatbot."),
            (r'help|support', "Sure, I am here to help! What do you need assistance with?"),
            (r'what can you do', "I can answer your questions, chat with you, and assist with general information."),
            (r'who created you', "I was created by a helpful software engineer assistant."),
            (r'thank you|thanks', "You're very welcome!"),
            (r'bye|goodbye|see you', "Goodbye! Have a wonderful day!"),
            (r'what is ai|what is artificial intelligence', 
             "Artificial Intelligence is the simulation of human intelligence processes by machines, especially computer systems."),
            (r'what is python', "Python is a high-level, interpreted programming language known for its readability and versatility."),
            (r'how to learn python', "You can learn Python through online tutorials, interactive courses, and practice by building small projects."),
            (r'tell me a joke', "Why do programmers prefer dark mode? Because light attracts bugs!"),
            (r'what is the meaning of life', "That's a deep question! Many say it is to seek happiness and help others."),
        ]
def get_response(self, user_input):
    user_input = user_input.lower()
    for pattern, response in self.qa_pairs:
            if re.search(pattern, user_input):
                return response
        # If no pattern matched, fallback response
    return "I'm sorry, I don't know the answer to that. Could you please ask something else?"
def main():
    print("Welcome to the AI Chatbot! (type 'exit' to quit)")
    chatbot = SimpleAIChatbot()
    while True:
        user_input = input("> ")
        if user_input.strip().lower() in ('exit', 'quit'):
            print("Goodbye! Thanks for chatting.")
            break
        response = chatbot.get_response(user_input)
        print(response)
if __name__ == "__main__":
    
