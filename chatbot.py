def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! How can I assist you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!",
        "what is your name": "I am a simple chatbot! You can call me ChatGPT.",
        "who created you": "I was created by OpenAI!"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "I'm sorry, I don't understand that. Can you try asking something else?"

# Running the chatbot in a loop
print("Chatbot is running... Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Have a great day!")
        break
    print("Chatbot:", chatbot_response(user_input))
