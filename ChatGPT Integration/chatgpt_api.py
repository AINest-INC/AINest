# chatgpt_api.py
import openai

def generate_text(prompt, api_key, model="gpt-3.5-turbo"):
    """Generates text using the OpenAI ChatGPT API.

    Args:
        prompt (str): The prompt to send to the API.
        api_key (str): Your OpenAI API key.
        model (str): The OpenAI model to use (default: "gpt-3.5-turbo").

    Returns:
        str: The generated text if successful, None otherwise.
    """
    openai.api_key = api_key
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating text: {e}")
        return None

if __name__ == '__main__':
    # Example usage:
    api_key = "YOUR_OPENAI_API_KEY"
    prompt = "Write a short poem about AI."
    generated_text = generate_text(prompt, api_key)
    if generated_text:
        print("Generated Text:")
        print(generated_text)
    else:
        print("Failed to generate text.")
