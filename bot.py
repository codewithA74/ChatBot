import ollama

print("AI Chatbot Started")
print("Type 'exit' to stop.\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response["message"]["content"]

    print("\nAI:", answer)
    print()