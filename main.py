from chatgpt import call_chatgpt

def main():
    prompt = "ChatGPT activated"
    response = call_chatgpt(prompt)
    print("ChatGPT Response:", response)

if __name__ == "__main__":
    main()
