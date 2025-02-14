# deepseek_api.py
import requests
import json

def generate_code(prompt, api_key, model="deepseek-coder"):
    """Generates code using the DeepSeek API.

    Args:
        prompt (str): The prompt to send to the API.
        api_key (str): Your DeepSeek API key.
        model (str): The DeepSeek model to use (default: "deepseek-coder").

    Returns:
        str: The generated code if successful, None otherwise.
    """
    url = "https://api.deepseek.com/v1/completions"  # Replace with actual DeepSeek API endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7
    })

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()["choices"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        print(f"Error generating code: {e}")
        return None

if __name__ == '__main__':
    # Example usage:
    api_key = "YOUR_DEEPSEEK_API_KEY"
    prompt = "Write a Python function to calculate the factorial of a number."
    generated_code = generate_code(prompt, api_key)
    if generated_code:
        print("Generated Code:")
        print(generated_code)
    else:
        print("Failed to generate code.")
