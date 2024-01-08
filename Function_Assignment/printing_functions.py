
def show_messages(messages):
    for message in messages:
        print(message)
messages = ['Hello, how are you?', 'What are you up to?', 'Have a great day!']
show_messages(messages)

def send_messages(messages):
    sent_messages = []
    for message in messages:
        print(message)
        sent_messages.append(message)
    return sent_messages

messages = ['Hello, how are you?', 'What are you up to?', 'Have a great day!']
sent_messages = send_messages(messages[:])
print(f"Original messages: {messages}")
print(f"Sent messages: {sent_messages}")

