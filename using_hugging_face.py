import streamlit as st
from huggingface_hub import InferenceClient

# Initialize the Hugging Face Inference Client
# Replace 'YOUR_HF_TOKEN' with your actual Hugging Face API token
client = InferenceClient(api_key="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")

# Streamlit app title
st.title("چت بات")

# Text input for user prompt
prompt_input = st.text_input('Enter your prompt:')

# Button to submit the prompt
if st.button("Generate Response"):
    if prompt_input:
        try:
            # Prepare messages for the chat
            messages = [
                {"role": "user", "content": prompt_input}
            ]
            
            # Create chat completion with Qwen2.5-72B-Instruct model
            response = client.chat.completions.create(
                model="Qwen/Qwen2.5-72B-Instruct", 
                messages=messages, 
                temperature=0.5,
                max_tokens=2048,
                top_p=0.7
            )
            
            # Display the response
            st.markdown(response.choices[0].message.content)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")