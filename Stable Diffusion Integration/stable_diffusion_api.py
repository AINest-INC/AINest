# stable_diffusion_api.py
import requests
import io
from PIL import Image

def generate_image(prompt, api_key, engine_id="stable-diffusion-xl-1024-v1-0"):
    """Generates an image using the Stability AI Stable Diffusion API.

    Args:
        prompt (str): The prompt to send to the API.
        api_key (str): Your Stability AI API key.
        engine_id (str): The engine ID to use (default: "stable-diffusion-xl-1024-v1-0").

    Returns:
        PIL.Image.Image: The generated image if successful, None otherwise.
    """
    url = f"https://api.stability.ai/v1/generation/{engine_id}/text-to-image"

    headers = {
        "Content-Type": "application/json",
        "Accept": "image/png",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "text_prompts": [
            {
                "text": prompt
            }
        ],
        "width": 512,
        "height": 512,
        "samples": 1,
        "steps": 30,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        image_data = io.BytesIO(response.content)
        image = Image.open(image_data)
        return image
    except requests.exceptions.RequestException as e:
        print(f"Error generating image: {e}")
        return None

if __name__ == '__main__':
    # Example usage:
    api_key = "YOUR_STABILITY_AI_API_KEY"
    prompt = "A futuristic cityscape at sunset."
    image = generate_image(prompt, api_key)
    if image:
        image.save("futuristic_city.png")
        print("Image generated and saved to futuristic_city.png")
    else:
        print("Failed to generate image.")
