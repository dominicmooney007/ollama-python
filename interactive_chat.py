from ollama import chat

def interactive_chat():
    print("Interactive chat with Ollama gemma3:1b model")
    print("Type 'quit' or 'exit' to end the conversation")
    print("-" * 50)

    messages = []

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break

        if not user_input:
            continue

        # Add user message to conversation history
        messages.append({
            'role': 'user',
            'content': user_input
        })

        try:
            # Get response from Ollama
            response = chat('gemma3:1b', messages=messages)
            assistant_message = response['message']['content']

            # Add assistant response to conversation history
            messages.append({
                'role': 'assistant',
                'content': assistant_message
            })

            print(f"\nAssistant: {assistant_message}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    interactive_chat()
