from ollama import Client

# Create a client connecting to the local Ollama server
client = Client("http://localhost:11434")

# Pull the model first to ensure it's available
try:
    client.pull('qwen2:0.5b')
except Exception as e:
    print(f"Error pulling model: {e}")

# Prepare the messages for the chat interaction
messages = [
    {
        "role": "user",
        "content": "Tell me a joke"
    }
]

# Send the chat request to the Ollama model
response = client.chat(
    model='qwen2:0.5b',
    messages=messages
)

# Print the AI's response
print(response['message'])
