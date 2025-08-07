import openai

key = "Your_API_key"  # Replace or better: use os.getenv()

client = openai.OpenAI(
    api_key=key
)

messages = []

def completion(message):
    global messages
    messages.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    assistant_message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    messages.append(assistant_message)
    print(f"Jarvis: {assistant_message['content']}")

if __name__ == "__main__":
    print("Jarvis: Hey I'm Jarvis, how can I help you?\n")
    while True:
        user_question = input("User: ")
        completion(user_question)
