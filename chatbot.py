import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Pairs = [pattern, list of possible responses]
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hey there! What can I do for you?"]],
    [r"what is your name?", ["I'm SupportBot, your assistant!"]],
    [r"how are you?", ["I'm doing great! How about you?"]],
    [r"what can you do?", ["I can answer FAQs, help with support queries, and have a conversation with you!"]],
    [r"(.*) your hours (.*)", ["We are available 24/7 for your support!"]],
    [r"(.*) refund (.*)", ["Please contact support@company.com for refund requests."]],
    [r"(.*) order (.*)", ["You can track your order at our website under 'My Orders'."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Feel free to come back anytime."]],
    [r"(.*)", ["I'm not sure about that. Can you rephrase?", "Could you clarify that a bit more?"]],
]

def get_response(user_input):
    chatbot = Chat(pairs, reflections)
    response = chatbot.respond(user_input)
    return response if response else "Sorry, I didn't understand that."