from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")

messages = [
	{ "role": "user", "content": "Tell me a story" }
]

completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-72B-Instruct", 
	messages=messages, 
	temperature=0.5,
	max_tokens=2048,
	top_p=0.7
)

print(completion.choices[0].message)