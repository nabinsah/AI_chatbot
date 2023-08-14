from parameter.conversation import chat_conversation
from parameter.mapping import mapping as mp_func


def main():
    chat_conversation.greeting()
    while True:
        data = input(f'nabin: ')
        mp_func(data)
    

if __name__ == "__main__":
    main()