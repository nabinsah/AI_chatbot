from parameter.conversation import chat_conversation as chat
import math

def mapping(data):

    if "day" in data:
        chat.day()
    
    elif "date" in data:
        chat.day()

    elif "time" in data:
        chat.time()

    elif "news" in data:
        chat.news()

    elif "temperature" in data:
        temp= chat.get_temperature()
        formatted_number = f"{temp:.2f}"
        print(f"The current temperature is : formatted_number degree celcius.")

    elif "weather" in data:
        print(f"The current weather is {chat.get_weather()}.")

    elif "exit" in data:
        chat.Exit()