import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def chatbot():
    speak("Welcome to CodeAlpha Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            speak("Hi there!")
        elif "how are you" in user_input:
            speak("I'm just a bot, but I'm doing great!")
        elif "your name" in user_input:
            speak("I'm CodeAlpha Chatbot.")
        elif "bye" in user_input or "exit" in user_input:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("Sorry, I didn't understand that.")

chatbot()
